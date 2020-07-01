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
        example: "camila"
      status:
        type: boolean
        required: true
        example: true
      enviroment:
        type: string
        required: true
        example: "enviroment name"
      version:
        type: string
        required: true
        example: 1
      address:
        type: string
        required: true
        example: "machine adress"
  Event:
    type: object
    discriminator: level
    properties:
      level: object
      payload:
        type: string
        required: true
        example: "payload"
      shelve:
        type: boolean
        required: true
        example: true
      data:
        type: datetime
        required: true
        example: "01-07-2020"
  Group:
    type: object
    discriminator: group
    properties:
      group: object
      name:
        type: string
        required: true
        example: "Apis para telefonia"
  User:
    type: object
    discriminator: user
    properties:
      user: object
      name:
        type: string
        required: true
        example: "camilanb"
      email:
        type: string
        pattern: ^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$
        required: true
        example: "user@user.com"
      password:
        type: string
        required: true
        example: "123456"
      last_login:
        type: datetime
        required: false
        example: "30-06-2020"


/auth/token:
  post:
    description: create token 
    body:
      type: Auth
      username: string
      password: string
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


/agents: 
  post:
    description:  create an agent
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

  get:
    description: get agents data
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
  /{id}:
    delete:
      description: delete agent data
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
    get: 
      description: get events data
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
    delete: 
      description: delete event data
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
            type: Erro no servido

  /{id}/events/{id}:
     post:
      description: create event
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

     get:
      description: get event by id
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

     delete: 
      description: delete event
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
  get: 
    description: get groups data
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
  /{id}:
    delete: 
      description: delete group by id
      securedBy: [JWT]
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
  get: 
    description: get users data
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
  /{id}:
    delete: 
      description: delete user by id
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
