expected_router_schema1 = {
    '/B/consumer-path/::method_1': {
        'post': {
            'operationId': 'method_1_send',
            'summary': 'method_1 summary',
            'description': 'method_1 description',
            'tags': ['web_socket'],
            'responses': {
                '200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/B/consumer-path/::method_2': {
        'post': {
            'operationId': 'method_2_send',
            'summary': 'method_2 summary',
            'description': 'method_2 description',
            'tags': ['web_socket'],
            'responses': {
                '201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                },
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/B/consumer-path/::method_3': {
        'get': {
            'operationId': 'method_3_receive',
            'summary': 'method_3 summary',
            'description': 'method_3 description',
            'tags': ['web_socket'],
            'responses': {
                '200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
        }
    },
    '/B/consumer-path/::method_4': {
        'get': {
            'operationId': 'method_4_receive',
            'summary': 'method_4 summary',
            'description': 'method_4 description',
            'tags': ['web_socket'],
            'responses': {
                '201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                },
            },
        }
    },
    '/B/consumer-path/::method_5': {
        'post': {
            'operationId': 'method_5_send',
            'summary': 'method_5 summary',
            'description': 'method_5 description',
            'tags': ['web_socket'],
            'responses': None,
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/B/consumer-path/::method_6': {
        'post': {
            'operationId': 'method_6_send',
            'summary': 'method_6 summary',
            'description': 'method_6 description',
            'tags': ['web_socket'],
            'responses': None,
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/B/consumer-path/::method_7': {
        'post': {
            'operationId': 'method_7_send',
            'summary': 'method_7 summary',
            'description': 'method_7 description',
            'tags': ['web_socket'],
            'responses': {
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                }
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_1': {
        'post': {
            'operationId': 'method_1_send',
            'summary': 'method_1 summary',
            'description': 'method_1 description',
            'tags': ['web_socket'],
            'responses': {
                '200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_2': {
        'post': {
            'operationId': 'method_2_send',
            'summary': 'method_2 summary',
            'description': 'method_2 description',
            'tags': ['web_socket'],
            'responses': {
                '201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                },
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_3': {
        'get': {
            'operationId': 'method_3_receive',
            'summary': 'method_3 summary',
            'description': 'method_3 description',
            'tags': ['web_socket'],
            'responses': {
                '200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_4': {
        'get': {
            'operationId': 'method_4_receive',
            'summary': 'method_4 summary',
            'description': 'method_4 description',
            'tags': ['web_socket'],
            'responses': {
                '201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                },
            },
        }
    },
    '/A/AA/consumer-path/::method_5': {
        'post': {
            'operationId': 'method_5_send',
            'summary': 'method_5 summary',
            'description': 'method_5 description',
            'tags': ['web_socket'],
            'responses': None,
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_6': {
        'post': {
            'operationId': 'method_6_send',
            'summary': 'method_6 summary',
            'description': 'method_6 description',
            'tags': ['web_socket'],
            'responses': None,
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_7': {
        'post': {
            'operationId': 'method_7_send',
            'summary': 'method_7 summary',
            'description': 'method_7 description',
            'tags': ['web_socket'],
            'responses': {
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                }
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_1': {
        'post': {
            'operationId': 'method_1_send',
            'summary': 'method_1 summary',
            'description': 'method_1 description',
            'tags': ['web_socket'],
            'responses': {
                '200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_2': {
        'post': {
            'operationId': 'method_2_send',
            'summary': 'method_2 summary',
            'description': 'method_2 description',
            'tags': ['web_socket'],
            'responses': {
                '201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                },
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_3': {
        'get': {
            'operationId': 'method_3_receive',
            'summary': 'method_3 summary',
            'description': 'method_3 description',
            'tags': ['web_socket'],
            'responses': {
                '200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_4': {
        'get': {
            'operationId': 'method_4_receive',
            'summary': 'method_4 summary',
            'description': 'method_4 description',
            'tags': ['web_socket'],
            'responses': {
                '201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                },
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_5': {
        'post': {
            'operationId': 'method_5_send',
            'summary': 'method_5 summary',
            'description': 'method_5 description',
            'tags': ['web_socket'],
            'responses': None,
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_6': {
        'post': {
            'operationId': 'method_6_send',
            'summary': 'method_6 summary',
            'description': 'method_6 description',
            'tags': ['web_socket'],
            'responses': None,
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_7': {
        'post': {
            'operationId': 'method_7_send',
            'summary': 'method_7 summary',
            'description': 'method_7 description',
            'tags': ['web_socket'],
            'responses': {
                '400': {
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                        }
                    },
                    'description': '',
                }
            },
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
        }
    },
}

expected_schema_1 = {
    'openapi': '3.0.3',
    'info': {'title': '', 'version': '0.0.0'},
    'paths': {
        '/B/consumer-path/::method_1': {
            'post': {
                'operationId': 'method_1_send_3',
                'summary': 'method_1 summary',
                'description': 'method_1 description',
                'tags': ['web_socket'],
                'responses': {
                    '200': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/B/consumer-path/::method_2': {
            'post': {
                'operationId': 'method_2_send_3',
                'summary': 'method_2 summary',
                'description': 'method_2 description',
                'tags': ['web_socket'],
                'responses': {
                    '201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/B/consumer-path/::method_3': {
            'get': {
                'operationId': 'method_3_receive_3',
                'summary': 'method_3 summary',
                'description': 'method_3 description',
                'tags': ['web_socket'],
                'responses': {
                    '200': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
            }
        },
        '/B/consumer-path/::method_4': {
            'get': {
                'operationId': 'method_4_receive_3',
                'summary': 'method_4 summary',
                'description': 'method_4 description',
                'tags': ['web_socket'],
                'responses': {
                    '201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                },
            }
        },
        '/B/consumer-path/::method_5': {
            'post': {
                'operationId': 'method_5_send_3',
                'summary': 'method_5 summary',
                'description': 'method_5 description',
                'tags': ['web_socket'],
                'responses': None,
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/B/consumer-path/::method_6': {
            'post': {
                'operationId': 'method_6_send_3',
                'summary': 'method_6 summary',
                'description': 'method_6 description',
                'tags': ['web_socket'],
                'responses': None,
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/B/consumer-path/::method_7': {
            'post': {
                'operationId': 'method_7_send_3',
                'summary': 'method_7 summary',
                'description': 'method_7 description',
                'tags': ['web_socket'],
                'responses': {
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AA/consumer-path/::method_1': {
            'post': {
                'operationId': 'method_1_send',
                'summary': 'method_1 summary',
                'description': 'method_1 description',
                'tags': ['web_socket'],
                'responses': {
                    '200': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AA/consumer-path/::method_2': {
            'post': {
                'operationId': 'method_2_send',
                'summary': 'method_2 summary',
                'description': 'method_2 description',
                'tags': ['web_socket'],
                'responses': {
                    '201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AA/consumer-path/::method_3': {
            'get': {
                'operationId': 'method_3_receive',
                'summary': 'method_3 summary',
                'description': 'method_3 description',
                'tags': ['web_socket'],
                'responses': {
                    '200': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
            }
        },
        '/A/AA/consumer-path/::method_4': {
            'get': {
                'operationId': 'method_4_receive',
                'summary': 'method_4 summary',
                'description': 'method_4 description',
                'tags': ['web_socket'],
                'responses': {
                    '201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                },
            }
        },
        '/A/AA/consumer-path/::method_5': {
            'post': {
                'operationId': 'method_5_send',
                'summary': 'method_5 summary',
                'description': 'method_5 description',
                'tags': ['web_socket'],
                'responses': None,
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AA/consumer-path/::method_6': {
            'post': {
                'operationId': 'method_6_send',
                'summary': 'method_6 summary',
                'description': 'method_6 description',
                'tags': ['web_socket'],
                'responses': None,
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AA/consumer-path/::method_7': {
            'post': {
                'operationId': 'method_7_send',
                'summary': 'method_7 summary',
                'description': 'method_7 description',
                'tags': ['web_socket'],
                'responses': {
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_1': {
            'post': {
                'operationId': 'method_1_send_2',
                'summary': 'method_1 summary',
                'description': 'method_1 description',
                'tags': ['web_socket'],
                'responses': {
                    '200': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_2': {
            'post': {
                'operationId': 'method_2_send_2',
                'summary': 'method_2 summary',
                'description': 'method_2 description',
                'tags': ['web_socket'],
                'responses': {
                    '201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_3': {
            'get': {
                'operationId': 'method_3_receive_2',
                'summary': 'method_3 summary',
                'description': 'method_3 description',
                'tags': ['web_socket'],
                'responses': {
                    '200': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_4': {
            'get': {
                'operationId': 'method_4_receive_2',
                'summary': 'method_4 summary',
                'description': 'method_4 description',
                'tags': ['web_socket'],
                'responses': {
                    '201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_5': {
            'post': {
                'operationId': 'method_5_send_2',
                'summary': 'method_5 summary',
                'description': 'method_5 description',
                'tags': ['web_socket'],
                'responses': None,
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_6': {
            'post': {
                'operationId': 'method_6_send_2',
                'summary': 'method_6 summary',
                'description': 'method_6 description',
                'tags': ['web_socket'],
                'responses': None,
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
        '/A/AB/AAA/consumer-path/::method_7': {
            'post': {
                'operationId': 'method_7_send_2',
                'summary': 'method_7 summary',
                'description': 'method_7 description',
                'tags': ['web_socket'],
                'responses': {
                    '400': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/BadOutputSerializer'}
                            }
                        },
                        'description': '',
                    }
                },
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
            }
        },
    },
    'components': {
        'schemas': {
            'BadOutputSerializer': {
                'type': 'object',
                'properties': {'field5': {'type': 'string'}, 'field6': {'type': 'integer'}},
                'required': ['field5', 'field6'],
            },
            'InputSerializer': {
                'type': 'object',
                'properties': {'field1': {'type': 'string'}, 'field2': {'type': 'integer'}},
                'required': ['field1', 'field2'],
            },
            'OutputSerializer': {
                'type': 'object',
                'properties': {'field3': {'type': 'string'}, 'field4': {'type': 'integer'}},
                'required': ['field3', 'field4'],
            },
        }
    },
}
