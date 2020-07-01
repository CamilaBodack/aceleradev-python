doc = """
title: API Modulo 8
baseUri: http://modulo8.com/{version}
version: v1
mediaType: aplication/json


securitySchemes:
  JWT:
    type: object
    discriminator: jwt
    properties:
      jwt: string


types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string
  Agent:
    type: object
    name:
      type: string
    status:
      type: boolean
    enviroment:
      type: string
    version:
      type: string
    address:
      type: string
  Event:
    type: object
    level:
      type: string
    payload:
      type: string
    email:
      type: string
      pattern: ^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$
    shelve:
      type: boolean
    data:
      type: datetime
  Group:
    type: object
    name:
      type: string
  User:
    type: object
    password:
      type: string
    last_login:
      type: datetime


/auth/token:
  post: 
    body:
      type: string


/agents: 
  is: [secured]
  post: 
    body:
      type: object
  get: 
    queryParameters:
      name:
  /{id}:
    delete:
    put:
      body:
  /{id}/events:
    post: 
      body:
        type: object
    get: 
      queryParameters:
    delete: 
    put:
      body:
  /{id}/events/{id}:
     post: 
      body:
        type: object
     get: 
      queryParameters:
     delete: 
     put:
      body:

/groups: 
  post:
    body:
      type:
  get: 
    queryParameters:
  /{id}:
    delete: 
    put:
      body:

/users: 
  post:
    body:
      type:
  get: 
    queryParameters:
  /{id}:
    delete: 
    put:
      body:
    
"""
