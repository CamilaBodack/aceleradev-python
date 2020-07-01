doc = """
#%RAML 1.0
title: API Modulo 8
baseUri: http://modulo8.com/{version}
version: v1
protocols: [HTTP, HTTPS]
mediaType: aplication/json


securitySchemes:
  JWT:
    description: API access is provided through JWT Token.
    type: jwt
    describedBy:
      headers:
        Authorization:
          description: |
              JSON Web Token (JWT) is an open standard (RFC 7519)
              that defines a compact and self-contained way for securely
              transmitting information between parties as a JSON object.
              This information can be verified and trusted because it is
              digitally signed. JWTs can be signed using a secret (with the HMAC algorithm)
              or a public/private key pair using RSA or ECDSA.
          type: string
      queryParameters:
        access_token:
          description: |
             A valid JWT to access API needs to be provided.
             Expiration time - 8 hours
          type: string
      responses:
        401:
          description: Invalid data
        500:
          description: server error
              

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string
  Agent:
    type: object
    discriminator: agent
    properties:
      agent: object
      name:
        type: string
        required: true
      status:
        type: boolean
        required: true
      enviroment:
        type: string
        required: true
      version:
        type: string
        required: true
      address:
        type: string
        required: true
    example: camila, true, cloud, v1, centro
  Event:
    type: object
    discriminator: level
    properties:
      level: object
      payload:
        type: string
        required: true
      shelve:
        type: boolean
        required: false
      data:
        type: datetime
        required: true
    example: critical, data, true, 01:07:2020
  Group:
    type: object
    discriminator: group
    properties:
      group: object
      name:
        type: string
        required: true
    example: Apis para telefonia
  User:
    type: object
    discriminator: user
    properties:
      user: object
      name:
        type: string
        required: true
      email:
        type: string
        pattern: ^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$
        required: true
      password:
        type: string
        required: true
      last_login:
        type: datetime
        required: false
    example: camila, user@user.com, senha, 30:06:2020 


/auth/token:
  post: 
    body:
      type: string


/agents: 
  post:
    description:  create an agent
    securedBy: [JWT]   
    body:
      type: object  
  get:
    description: get agents data 
    queryParameters:  
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
  /{id}:
    delete:
      description: delete agent data
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor

    put:
      description: update agent data
      securedBy: [JWT]  
      body:
        type: Agent
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor


  /{id}/events:
    post:
      securedBy: [JWT]   
      description: create event
      body:
        type: Event
    get: 
      description: get events data
      queryParameters:  
    delete: 
      description: delete event data
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor
    put:
      description: update event data
      securedBy: [JWT]  
      body:
        type: Event
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor

  /{id}/events/{id}:

     post:
      description: create event
      securedBy: [JWT]  
      body:
        type: object
     get:
      description: get event by id
      queryParameters:

     delete: 
      description: delete event
      responses:
        body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor
     put:
      description: update event data
      securedBy: [JWT]  
      body:
        type: Event
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor

/groups:
  post:
    description: create group
    securedBy: [JWT]  
    body:
      type: Group
  get: 
    description: get groups data
    queryParameters:
      name:
        type: string
  /{id}:
    delete: 
      description: delete group by id
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor
    put:
      description: update group data
      securedBy: [JWT]  
      body:
        type: Group
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor


/users:
  post:
    description: create user
    securedBy: [JWT]  
    body:
      type: User
  get: 
    description: get users data
    queryParameters:
  /{id}:
    delete: 
      description: delete user by id
      responses:
      200:
        body:
          type: Operação realizada com sucesso
      401:
        body:
          type: Erro na operação
      500:
        body:
          type: Erro no servidor
    put:
      description: update user data
      securedBy: [JWT]  
      body:
        type: User
      responses:
        200:
          body:
            type: Operação realizada com sucesso
        401:
          body:
            type: Erro na operação
        500:
          body:
            type: Erro no servidor

"""
