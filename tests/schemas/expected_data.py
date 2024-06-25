expected_router_schema1 = {
    '/B/consumer-path/::method_1': {
        'post': {
            'operationId': 'method_1_send',
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
            'summary': 'method_1 summary',
            'description': 'method_1 description',
            'tags': ['web_socket'],
            'responses': {
                'method_1\xa0\xa0\xa0200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
        }
    },
    '/B/consumer-path/::method_2': {
        'post': {
            'operationId': 'method_2_send',
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
            'summary': 'method_2 summary',
            'description': 'method_2 description',
            'tags': ['web_socket'],
            'responses': {
                'method_2\xa0\xa0\xa0201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                'method_2\xa0\xa0\xa0400': {
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
    '/B/consumer-path/::method_3': {
        'get': {
            'operationId': 'method_3_receive',
            'requestBody': None,
            'summary': 'method_3 summary',
            'description': 'method_3 description',
            'tags': ['web_socket'],
            'responses': {
                'method_3\xa0\xa0\xa0200': {
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
            'requestBody': None,
            'summary': 'method_4 summary',
            'description': 'method_4 description',
            'tags': ['web_socket'],
            'responses': {
                'method_4\xa0\xa0\xa0201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                'method_4\xa0\xa0\xa0400': {
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
    '/A/AA/consumer-path/::method_1': {
        'post': {
            'operationId': 'method_1_send',
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
            'summary': 'method_1 summary',
            'description': 'method_1 description',
            'tags': ['web_socket'],
            'responses': {
                'method_1\xa0\xa0\xa0200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
        }
    },
    '/A/AA/consumer-path/::method_2': {
        'post': {
            'operationId': 'method_2_send',
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
            'summary': 'method_2 summary',
            'description': 'method_2 description',
            'tags': ['web_socket'],
            'responses': {
                'method_2\xa0\xa0\xa0201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                'method_2\xa0\xa0\xa0400': {
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
    '/A/AA/consumer-path/::method_3': {
        'get': {
            'operationId': 'method_3_receive',
            'requestBody': None,
            'summary': 'method_3 summary',
            'description': 'method_3 description',
            'tags': ['web_socket'],
            'responses': {
                'method_3\xa0\xa0\xa0200': {
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
            'requestBody': None,
            'summary': 'method_4 summary',
            'description': 'method_4 description',
            'tags': ['web_socket'],
            'responses': {
                'method_4\xa0\xa0\xa0201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                'method_4\xa0\xa0\xa0400': {
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
    '/A/AB/AAA/consumer-path/::method_1': {
        'post': {
            'operationId': 'method_1_send',
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
            'summary': 'method_1 summary',
            'description': 'method_1 description',
            'tags': ['web_socket'],
            'responses': {
                'method_1\xa0\xa0\xa0200': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                }
            },
        }
    },
    '/A/AB/AAA/consumer-path/::method_2': {
        'post': {
            'operationId': 'method_2_send',
            'requestBody': {
                'content': {
                    'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                }
            },
            'summary': 'method_2 summary',
            'description': 'method_2 description',
            'tags': ['web_socket'],
            'responses': {
                'method_2\xa0\xa0\xa0201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                'method_2\xa0\xa0\xa0400': {
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
    '/A/AB/AAA/consumer-path/::method_3': {
        'get': {
            'operationId': 'method_3_receive',
            'requestBody': None,
            'summary': 'method_3 summary',
            'description': 'method_3 description',
            'tags': ['web_socket'],
            'responses': {
                'method_3\xa0\xa0\xa0200': {
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
            'requestBody': None,
            'summary': 'method_4 summary',
            'description': 'method_4 description',
            'tags': ['web_socket'],
            'responses': {
                'method_4\xa0\xa0\xa0201': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/OutputSerializer'}}
                    },
                    'description': '',
                },
                'method_4\xa0\xa0\xa0400': {
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
}

expected_schema_1 = {
    'openapi': '3.0.3',
    'info': {'title': '', 'version': '0.0.0'},
    'paths': {
        '/B/consumer-path/::method_1': {
            'post': {
                'operationId': 'method_1_send_3',
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
                'summary': 'method_1 summary',
                'description': 'method_1 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_1\xa0\xa0\xa0200': {
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
        '/B/consumer-path/::method_2': {
            'post': {
                'operationId': 'method_2_send_3',
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
                'summary': 'method_2 summary',
                'description': 'method_2 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_2\xa0\xa0\xa0201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    'method_2\xa0\xa0\xa0400': {
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
        '/B/consumer-path/::method_3': {
            'get': {
                'operationId': 'method_3_receive_3',
                'requestBody': None,
                'summary': 'method_3 summary',
                'description': 'method_3 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_3\xa0\xa0\xa0200': {
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
                'requestBody': None,
                'summary': 'method_4 summary',
                'description': 'method_4 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_4\xa0\xa0\xa0201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    'method_4\xa0\xa0\xa0400': {
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
        '/A/AA/consumer-path/::method_1': {
            'post': {
                'operationId': 'method_1_send',
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
                'summary': 'method_1 summary',
                'description': 'method_1 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_1\xa0\xa0\xa0200': {
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
        '/A/AA/consumer-path/::method_2': {
            'post': {
                'operationId': 'method_2_send',
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
                'summary': 'method_2 summary',
                'description': 'method_2 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_2\xa0\xa0\xa0201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    'method_2\xa0\xa0\xa0400': {
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
        '/A/AA/consumer-path/::method_3': {
            'get': {
                'operationId': 'method_3_receive',
                'requestBody': None,
                'summary': 'method_3 summary',
                'description': 'method_3 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_3\xa0\xa0\xa0200': {
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
                'requestBody': None,
                'summary': 'method_4 summary',
                'description': 'method_4 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_4\xa0\xa0\xa0201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    'method_4\xa0\xa0\xa0400': {
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
        '/A/AB/AAA/consumer-path/::method_1': {
            'post': {
                'operationId': 'method_1_send_2',
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
                'summary': 'method_1 summary',
                'description': 'method_1 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_1\xa0\xa0\xa0200': {
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
        '/A/AB/AAA/consumer-path/::method_2': {
            'post': {
                'operationId': 'method_2_send_2',
                'requestBody': {
                    'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/InputSerializer'}}
                    }
                },
                'summary': 'method_2 summary',
                'description': 'method_2 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_2\xa0\xa0\xa0201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    'method_2\xa0\xa0\xa0400': {
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
        '/A/AB/AAA/consumer-path/::method_3': {
            'get': {
                'operationId': 'method_3_receive_2',
                'requestBody': None,
                'summary': 'method_3 summary',
                'description': 'method_3 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_3\xa0\xa0\xa0200': {
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
                'requestBody': None,
                'summary': 'method_4 summary',
                'description': 'method_4 description',
                'tags': ['web_socket'],
                'responses': {
                    'method_4\xa0\xa0\xa0201': {
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/OutputSerializer'}
                            }
                        },
                        'description': '',
                    },
                    'method_4\xa0\xa0\xa0400': {
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
