"use strict";

function _isWs(value) {
  return value.toLowerCase().includes("::")
}

const regex = /^(?<path>.+)::(?<name>.+)$/gm

function getPath(wsPathName) {
  regex.lastIndex = 0
  const match = regex.exec(wsPathName)
  if (match) {
    return match.groups.path
  }
}

function getName(wsPathName) {
  regex.lastIndex = 0
  const match = regex.exec(wsPathName)
  if (match) {
    return match.groups.name
  }
}

function getJwtToken() {
    let authorized;
    if (uiInitialized()) {
      const state = ui.getState().get("auth").get("authorized");
      if (state !== undefined && Object.keys(state.toJS()).length !== 0) {
        authorized = state.toJS();
      }
    } else if (![undefined, "{}"].includes(localStorage.authorized)) {
      authorized = JSON.parse(localStorage.authorized);
    }

    const token = authorized?.jwtAuth?.value

    if (typeof token !== 'undefined') {
      return `?token=${token}`
    };
    return ""
}

function makeSocket(socketActions, path) {
  socketActions.setStatus({path, status: "connecting..."})

  const scheme = window.location.protocol === 'https:' ? 'wss' : 'ws'
  const url = `${scheme}://${window.location.host}${path}` + getJwtToken()

  let socket = new WebSocket(url)

  socket.onmessage = (message) => {
    socketActions.addMessage({
      path,
      message: JSON.parse(message.data),
      type: "receive",
    })
  }

  socket.onopen = () => {
    socketActions.setStatus({path, status: "opened"})
  }

  socket.onclose = (event) => {
    socketActions.setStatus({path, status: "closed"})
    setTimeout(() => {
      makeSocket(socketActions, path)
    }, 3000)  // задержка перед переподключением WS
  }

  socket.onerror = () => {
    socketActions.setStatus({path, status: "error"})
    socket.close()
  }

  socketActions.storeSocket({path, socket})
}

const socketEventsPlugin = function (system) {
  return {
    statePlugins: {
      spec: {
        selectors: {
          socketUrl: (state) => {
            const urls = new Set()
            const paths = system.specSelectors.paths(state)
            paths.forEach((path, pathName) => {
              const wsPath = getPath(pathName)
              if (wsPath) {
                urls.add(wsPath)
              }
            })

            return urls
          },
          socketOperations: (state) => {
            const operations = []
            const paths = system.specSelectors.paths(state)
            paths.forEach((path, pathName) => {
              if (!path || !path.forEach) {
                return {}
              }
              path.forEach((operation, method) => {
                if (["send", "receive"].indexOf(method) < 0) {
                  return
                }
                operations.push({
                  path: pathName,
                  method,
                  operation,
                  id: `${method}-${pathName}`
                })
              })
            })
            return operations
          }
        },
        wrapSelectors: {
          allowTryItOutFor: (ori) => (object, path, schema) => {
            return !_isWs(path) || schema === "post"
          },
        },
        wrapActions: {
          executeRequest: (oriAction, system) => (args) => {
            const {pathName, method} = args
            const {oas3Selectors, socketActions, specActions, socketSelectors} = system
            if (_isWs(pathName)) {
              const path = getPath(pathName)
              const socket = socketSelectors.socket(path)
              if (socket && socket.readyState === WebSocket.OPEN) {
                const requestBody = oas3Selectors.requestBodyValue(pathName, method)
                socket.send(requestBody)
                socketActions.addMessage({
                  path,
                  message: JSON.parse(requestBody),
                  type: "send"
                })
                specActions.setMutatedRequest(pathName, method, {url: pathName})
                specActions.setResponse(pathName, method, {
                  headers: "",
                  status: 200,
                  url: pathName,
                  text: 'Message was send to socket! 😎'
                })
                return
              } else {
                specActions.setResponse(pathName, method, {
                  headers: "",
                  status: 418,
                  url: pathName,
                  text: 'Socket in closed state! 🤕'
                })
                return
              }
            }

            return oriAction(args)
          }
        },
      },
      socket: {
        actions: {
          storeSocket: ({path, socket}) => {
            return {
              type: "STORE_SOCKET",
              payload: {path, socket},
            }
          },
          setStatus: ({path, status}) => {
            return {
              type: "SOCKET_SET_STATUS",
              payload: {path, status},
            }
          },
          addMessage: ({path, message, type}) => {
            return {
              type: "SOCKET_ADD_MESSAGE",
              payload: {path, message, type},
            }
          },
          clearMessages: ({path}) => {
            return {
              type: "SOCKET_CLEAR_MESSAGES",
              payload: {path},
            }
          }
        },
        reducers: {
          "STORE_SOCKET": (state, {payload}) => {
            const {path, socket} = payload
            let sockets = state.get("sockets") || {}
            return state.set("sockets", {...sockets, [path]: socket})
          },

          "SOCKET_SET_STATUS": (state, {payload}) => {
            const {path, status} = payload
            let statuses = state.get("statuses") || {}
            return state.set("statuses", {...statuses, [path]: status})
          },

          "SOCKET_ADD_MESSAGE": (state, {payload}) => {
            const {path, message, type} = payload
            let messages = state.get("messages") || {}

            if (!(path in messages)) {
              messages[path] = []
            }
            messages[path].push({message, type})

            if (maxWSMessages && messages[path].length > maxWSMessages) {
              messages[path].shift()
            }

            return state.set("messages", {...messages})
          },

          "SOCKET_CLEAR_MESSAGES": (state, {payload}) => {
            const {path} = payload
            let messages = state.get("messages") || {}
            if (path in messages) {
              messages[path] = []
            }

            return state.set("messages", {...messages})
          }
        },
        selectors: {
          socket: (state, path) => {
            const sockets = state.get("sockets") || {}
            return sockets[path]
          },
          socketStatus: (state, path) => {
            const statuses = state.get("statuses") || {}
            return statuses[path] || "closed"
          },
          socketMessages: (state, path) => {
            const messages = state.get("messages") || {}
            return messages[path] || []
          },
          socketStatusMarker: (state, path) => {
            const statuses = state.get("statuses") || {}
            const status = statuses[path]
            switch (status) {
              case "opened":
                return "post"
              case "error":
                return "delete"
              case "closed":
              default:
                return "put"
            }
          }
        }
      }
    },
    fn: {
      makeSocket,
    },
    components: {
      WsResponse: ({event, response, getConfigs, method}) => {
        const {React, fn, getComponent} = system

        const HighlightCode = getComponent("highlightCode")
        const activeMediaType = response.getIn(["content", "application/json"])
        // const activeMediaType = response.getIn(["application/json"])

        const sampleResponse = fn.getSampleSchema(
          activeMediaType.get("schema"),
          "application/json",
          {"includeWriteOnly": true, "includeReadOnly": true},
        )

        let td_element = null
        if (method === "post") {
            td_element = React.createElement("td", {class: "response-col_event"},
              React.createElement("span", {
                  class: "opblock-summary-method",
                  style: {padding: 6, display: "inline-block"}
                },
                event
              )
            )
        }

        return React.createElement("tr", {},
          td_element,
          React.createElement("td", {class: "response-col_body", style: {width: "85%"}},
            React.createElement(HighlightCode, {
              class: "example",
              getConfigs,
              language: "json",
              value: sampleResponse
            }),
          )
        )
      },
      WsResponses: (props) => {
        const {React} = system
        const wsResponse = system.getComponent("WsResponse")
        const {responses, getConfigs} = props

        const method = props["method"]
        // method: get === RECEIVE
        // method: post === SEND

        const rows = responses.entrySeq().map(([event, response]) => React.createElement(wsResponse, {
          event, response, getConfigs, method
        },))

        let td_element = null
        if (method === "post") {
            td_element = React.createElement("td", {class: "col_header response-col_event"}, "Action name")
        }

        const table = React.createElement("table", {
            class: "responses-table",
            "aria-live": "polite",
            role: "region",
          },
          React.createElement("thead", {},
            React.createElement("tr", {class: "responses-header"},
              td_element,
              React.createElement("td", {class: "col_header response-col_body"}, "Responses body"),
            )
          ),
          React.createElement("tbody", {}, ...rows)
        )

        return React.createElement("div", {class: "responses-wrapper"},
          React.createElement("div", {class: "opblock-section-header"},
            React.createElement("h4", {}, "Receiving data")
          ),
          React.createElement("div", {class: "responses-inner"}, table)
        )
      },
      Message: ({message, type}) => {
        const {React, getComponent, getConfigs} = system

        const ResponseBody = getComponent("responseBody")

        const body = React.createElement(ResponseBody, {
          content: JSON.stringify(message),
          contentType: "application/json",
          getConfigs,
          getComponent
        })

        const background = type === "send" ? "#ffa500" : "#49cc90"
        return React.createElement("tr", {},
          React.createElement("td", {class: "response-col_event"},
            React.createElement("span", {
                class: "opblock-summary-method",
                style: {minWidth: 90, display: "inline-block", background}
              },
              type.toUpperCase()),
          ),
          React.createElement("td", {class: "response-col_description ws-message-response"}, body)
        )
      },
      SocketConnection({url, socketSelectors, socketActions, ...props}) {
        const {layoutSelectors, layoutActions} = props

        const {React} = system
        const prevSocket = socketSelectors.socket(url)
        if (!prevSocket && swaggerSettings.connectSocket) {
          system.fn.makeSocket(socketActions, url)
        }

        const Message = system.getComponent("Message")
        const ArrowUpIcon = system.getComponent("ArrowUpIcon")
        const ArrowDownIcon = system.getComponent("ArrowDownIcon")

        let isShown = layoutSelectors.isShown(['operations-tag', `ws-${url}`])

        if (isShown === undefined) {
          isShown = swaggerSettings.socketMessagesInitialOpened
        }

        function toggleShown() {
          layoutActions.show(['operations-tag', `ws-${url}`], !isShown)
        }

        const toggle = React.createElement("button",
          {class: "opblock-control-arrow", tabIndex: -1, onClick: toggleShown},
          isShown ? React.createElement(ArrowDownIcon, {class: "arrow"}) : React.createElement(ArrowUpIcon, {class: "arrow"}),
        )


        const clearMessages = () => {
          socketActions.clearMessages({path: url})
        }
        const socketStatus = socketSelectors.socketStatus(url)
        const socketStatusMarker = socketSelectors.socketStatusMarker(url)
        const socketMessages = socketSelectors.socketMessages(url)

        const receivedMsgsCount = socketMessages.filter((msg) => msg.type === "receive").length
        const sentMsgsCount = socketMessages.length - receivedMsgsCount
        const totalMsgs = `Total messages: sent: ${sentMsgsCount}, received: ${receivedMsgsCount}`

        let table = null

        if (isShown) {
          const messages = socketMessages.map(message => React.createElement(Message, message))

          table = React.createElement("table", {
              class: "responses-table",
              "aria-live": "polite",
              role: "region",
            },
            React.createElement("thead", {},
              React.createElement("tr", {class: "responses-header"},
                React.createElement("td", {class: "col_header response-col_event"}, "Type"),
                React.createElement("td", {class: "col_header response-col_body"}, "Body"),
              )
            ),
            React.createElement("tbody", {}, ...messages)
          )
        }


        const socketMessagesComponent = React.createElement("span", {},
          React.createElement("div", {
              class: "opblock opblock-get",
              id: `operations-tag-WS_connection_state-${url}`,
            },
            React.createElement("div", {class: "opblock-summary opblock-summary-get"},
              React.createElement("button", {class: "opblock-summary-control", onClick: toggleShown},
                React.createElement("span", {
                  class: `opblock-summary-method opblock-${socketStatusMarker}`,
                  style: {minWidth: 140}
                }, socketStatus.toUpperCase()),
                React.createElement("span", {class: "opblock-summary-path"}, ` WebSocket connection state: "${url}" `),
                React.createElement("span", {class: "opblock-summary-path"}, totalMsgs),
              ),
              React.createElement("button", {
                class: "btn ml-auto cancel",
                onClick: clearMessages,
              }, "Clear messages"),
              toggle,
            ),
            React.createElement("div", {class: "no-margin"},
              React.createElement("div", {class: "operation-tag-content"},
                isShown ? React.createElement("div", {class: "responses-inner"},
                      React.createElement("div", {class: "opblock-body"}, table)
                    ) : null,
              )
            )
          )
        )

        return React.createElement("div", {},
          React.createElement("style", {}, "td.ws-message-response h5 { display: none }"),
          socketMessagesComponent,
        )
      }
    },
    wrapComponents: {
      curl: (Original, {React}) => (props) => {
        let {request} = props
        let {url} = request.toJS()
        if (_isWs(url)) {
          return null
        }

        return React.createElement(Original, props)
      },
      parameters: (Original, {React}) => (props) => {
        const {pathMethod} = props
        const path = pathMethod[0]
        const schema = pathMethod[1]
        if (!_isWs(path) || schema === "post") {
          return React.createElement(Original, props)
        }
        return null
      },
      operations: (Original, {React}) => (props) => {
        const {specSelectors} = props

        const urls = specSelectors.socketUrl()
        const WsConnection = system.getComponent("SocketConnection")
        const socketComponents = []

        urls.forEach((url) => socketComponents.push(React.createElement(WsConnection, {
          url,
          ...props,
        })))

        return React.createElement("div", null,
          React.createElement(Original, props),
          ...socketComponents,
        )
      },
      OperationSummary: (Original, {React}) => (props) => {
        let {method, path} = props.operationProps.toJS()

        if (_isWs(path)) {
          switch (method) {
            case "post":
              method = "send"
              break
            case "get":
            default:
              method = "receive"
              break
          }
        }

        props.operationProps = props.operationProps.set("method", method)
        return React.createElement(Original, props)
      },
      responses: (Original, {React}) => (props) => {
        const {path} = props
        if (_isWs(path)) {
          const WsResponses = system.getComponent("WsResponses")
          return React.createElement(WsResponses, props)
        }
        return React.createElement(Original, props)
      }
    }
  }
}

const swaggerSettings = {{ settings|safe }};
const schemaAuthNames = {{ schema_auth_names|safe }};
let schemaAuthFailed = false;
const plugins = [socketEventsPlugin];

const getMaxMessages = () => {
  if (swaggerSettings.socketMaxMessages) {
    const max = swaggerSettings.socketMaxMessages
    return Number.parseInt(max) || 0
  }
  return 0
}

const maxWSMessages = getMaxMessages()

const reloadSchemaOnAuthChange = () => {
  return {
    statePlugins: {
      auth: {
        wrapActions: {
          authorize: (ori) => (...args) => {
            schemaAuthFailed = false;
            setTimeout(() => ui.specActions.download());
            return ori(...args);
          },
          logout: (ori) => (...args) => {
            schemaAuthFailed = false;
            setTimeout(() => ui.specActions.download());
            return ori(...args);
          },
        },
      },
    },
  };
};

if (schemaAuthNames.length > 0) {
  plugins.push(reloadSchemaOnAuthChange);
}

const uiInitialized = () => {
  try {
    ui;
    return true;
  } catch {
    return false;
  }
};

const isSchemaUrl = (url) => {
  if (!uiInitialized()) {
    return false;
  }
  return url === new URL(ui.getConfigs().url, document.baseURI).href;
};

const responseInterceptor = (response, ...args) => {
  if (!response.ok && isSchemaUrl(response.url)) {
    console.warn("schema request received '" + response.status + "'. disabling credentials for schema till logout.");
    if (!schemaAuthFailed) {
      // only retry once to prevent endless loop.
      schemaAuthFailed = true;
      setTimeout(() => ui.specActions.download());
    }
  }
  return response;
};

const injectAuthCredentials = (request) => {
  let authorized;
  if (uiInitialized()) {
    const state = ui.getState().get("auth").get("authorized");
    if (state !== undefined && Object.keys(state.toJS()).length !== 0) {
      authorized = state.toJS();
    }
  } else if (![undefined, "{}"].includes(localStorage.authorized)) {
    authorized = JSON.parse(localStorage.authorized);
  }
  if (authorized === undefined) {
    return;
  }
  for (const authName of schemaAuthNames) {
    const authDef = authorized[authName];
    if (authDef === undefined || authDef.schema === undefined) {
      continue;
    }
    if (authDef.schema.type === "http" && authDef.schema.scheme === "bearer") {
      request.headers["Authorization"] = "Bearer " + authDef.value;
      return;
    } else if (authDef.schema.type === "http" && authDef.schema.scheme === "basic") {
      request.headers["Authorization"] = "Basic " + btoa(authDef.value.username + ":" + authDef.value.password);
      return;
    } else if (authDef.schema.type === "apiKey" && authDef.schema.in === "header") {
      request.headers[authDef.schema.name] = authDef.value;
      return;
    }
  }
};

const requestInterceptor = (request, ...args) => {
  if (request.loadSpec && schemaAuthNames.length > 0 && !schemaAuthFailed) {
    try {
      injectAuthCredentials(request);
    } catch (e) {
      console.error("schema auth injection failed with error: ", e);
    }
  }
  // selectively omit adding headers to mitigate CORS issues.
  if (!["GET", undefined].includes(request.method) && request.credentials === "same-origin") {
    request.headers["{{ csrf_header_name }}"] = "{{ csrf_token }}";
  }
  return request;
};

const ui = SwaggerUIBundle({
  url: "{{ schema_url }}",
  dom_id: "#swagger-ui",
  presets: [SwaggerUIBundle.presets.apis],
  plugins,
  layout: "BaseLayout",
  requestInterceptor,
  responseInterceptor,
  ...swaggerSettings,
});

{% if oauth2_config %}ui.initOAuth({{ oauth2_config|safe }});{% endif %}
