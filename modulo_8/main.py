doc = """
#%RAML 1.0
title: API Modulo 8
baseUri: http://modulo8.com/{version}
version: v1
protocols: [HTTP, HTTPS]
mediaType: aplication/json
              
securitySchemes:
  JWT:
    description: A valid JWT to access API needs to be provided. Expiration time - 8 hours.
    type: x-jwt
    describedBy:
      headers:
        Authorization:
          description:
              JSON Web Token (JWT) is an open standard (RFC 7519)
              that defines a compact and self-contained way for securely
              transmitting information between parties as a JSON object.
          type: string
          required: true
      responses:
        body:
            200:
              description: Successfully logged in      
            401:
              description: Invalid data format or expired token.
    settings:
      signatures:['SHA256']

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string

  User:
   type: object
   discriminator: user_id
   properties:
      user_id: integer
      name: string
      email: string
      password: string
      last_login: datetime
   example:
      user_id: 1
      name: string
      email: example@example.com
      password: 123456
      last_login: 01-07-2020


  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id: integer
      user_id: integer
      name: string
      status: boolean
      environment: string
      version: string
      address: string
    example:
      agent_id: 33
      used_id: 27
      name: string
      status: true
      environment: enviroment
      version: v1
      address: ipv4 address

  Group:
    type: object
    discriminator: group_id
    properties:
      group_id: integer
      name: string
    example:
      group_id: 1
      name: string

  Event:
   type: object
   discriminator: event_id
   properties:
      event_id: integer
      agent_id: integer
      level: string
      payload: string
      shelve: boolean
      data: datetime
   example:
      event_id: 29
      agent_id: 25
      level: debug
      payload: string
      shelve: false
      data: 02-07-2020


/auth/token:
  post:
    description: Request token to acess API
    body:
      application/json:
          username: string
          password: string
    responses:
      201:
        body:
          application/json:
            type: Auth
      401:
        body:
          application/json:
            {"error": "Invalid data format or user not found"}

      404:
        body:
          application/json: |
            {"message": "Client error"}

/agents: 
  post:
    description:  create an agent
    securedBy: JWT
    body:
      application/json:  
        properties:
        example: |
          {"user_id": "1",
           "name": "username",
           "status": true,
           "environment": "type of environment",
           "version": "version used",
           "address": "ipv4 address"}
        responses:
          201:
            body:
              application/json: |
                example:
                  {"agent_id": }
          401:
            body:
              application/json:
                {"error": "Erro na operação"}

  get:
    description: get agents data
    securedBy: JWT
    responses:
      200:
        body:
          application/json: Agent[]

  /{id}:
    get:
      description: get agent data by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"message": "Erro na operação"}
        404:
          body:
            application/json: |
              {"message": "Client error"}

    delete:
      description: delete agent data
      securedBy: JWT
      body:
        responses:
          200:
            body:
              application/json: Agent
          401:
            body:
              application/json: |
                {"message": "Erro na operação"}
          404:
            body:
              application/json: |
                {"message": "Client error"}

    put:
      description: update agent data
      securedBy: JWT
      application/json:
        responses:
          200:
            body:
              application/json: Agent
          401:
            body:
              application/json: |
                {"message": "Erro na operação"}
          404:
            body:
              application/json: |
                {"message": "Client error"}


  /{id}/events:
    post:
      description: create event
      securedBy: JWT
      body:
        application/json: Event[]
        responses:
          201:
            body:
              application/json: |
                {"message": "event created"}
          401:
            body:
              application/json: |
                {"message": "Erro na operação"}
          404:
            body:
              application/json: |
                {"message": "Client error"}

    get: 
      description: get event data by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Event[]
        401:
          body:
            application/json: |
              {"message": "Operation error"}
        404:
          body:
            application/json: |
              {"message": "Client error"}
      
    delete: 
      description: delete event data
      securedBy: JWT
      body:
        application/json: Event[]
        200:
          body:
            application/json: |
              {"message": "Event deleted"}
        401:
          body:
            application/json: |
              {"message": "Operation error"}
        404:
          body:
            application/json: |
              {"message": "Client error"}

    put:
      description: update event data
      securedBy: JWT
      body:
        application/json: Event[]
        200:
           body:
             application/json: |
              {"message": "update events"}
        401:
          body:
            application/json: |
              {"message": "Operation error"}
        404:
         body:
           application/json: |
             {"message": "Client error"}

    /{id}:
        post:
          description: create event
          securedBy: JWT  
          body:
            application/json:
              responses:
              200:
                body:
                  application/json: Event
              401:
                body:
                  application/json: |
                    {"message": "Erro na operação"}
              404:
                body:
                  application/json: |
                    {"message": "Client error"}
      
        get:
          description: get event by id
          securedBy: JWT
          responses: 
            200:
              body:
                application/json: Event
            401:
              body:
                application/json:
                  {"message": "Erro na operação"}
            404:
               body:
                 application/json: |
                   {"message": "Client error"}
    
        delete: 
          description: delete event
          securedBy: JWT
          body:  
            responses:
              200:
                body:
                  application/json: |
                    {"message": "event deleted"}
              401:
                body:
                  application/json:
                    {"message": "Erro na operação"}
              404:
                 body:
                   application/json: |
                     {"message": "Client error"}
    
        put:
          description: update event data
          securedBy: JWT  
          body:
            application/json:
              responses:
                200:
                  body:
                    application/json: Event
                401:
                  body:
                    application/json: |
                      {"message": "Erro na operação"}
                404:
                  body:
                    application/json: |
                      {"message": "Client error"}
    
/groups:
  post:
    description: create group
    securedBy: JWT  
    body:
      application/json:
        properties:
          name: string
        example:
          {"name": "string"}
        responses:
          201:
            body:
              application/json: Group[]
          401:
            body:
              application/json:
                {"message": "Erro na operação"}
        
  get: 
    description: get groups data
    securedBy: JWT  
    responses:
      200:
        body:
          application/json: Group[]
      401:
        body:
          application/json:
            {"message": "Erro na operação"}

  put:
    description: update groups data
    securedBy: JWT  
    body:
      application/json:
        responses:
          200:
            body:
              application/json: Group[]
          401:
           body:
              application/json: |
                {"message": "Erro na operação"}
          404:
           body:
             application/json: |
               {"message": "Client error"}

  delete: 
    description: delete groups
    securedBy: JWT
    responses:
      200:
        body:
          application/json: |
            {"message": "group deleted"}
      401:
       body:
          application/json: |
            {"message": "Erro na operação"}
      404:
           body:
             application/json: |
               {"message": "Client error"}

  /{id}:
    post:
      description: create group
      securedBy: JWT  
      body:
        application/json:
          properties:
            name: string
          example:
            {"name": "string"}
          responses:
            201:
              body:
                application/json: Group
            401:
              body:
                application/json:
                  {"message": "Erro na operação"}

    get:
      description: get group data by id
      securedBy: JWT  
      responses:
        200:
          body:
            application/json: Group
        401:
          body:
            application/json:
              {"message": "Erro na operação"}
        404:
          body:
            application/json: |
              {"message": "Client error"}

    delete: 
      description: delete group by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "group deleted"}
        401:
         body:
            application/json: |
              {"message": "Erro na operação"}
        404:
           body:
             application/json: |
               {"message": "Client error"}

    put:
      description: update group data by id
      securedBy: JWT  
      body:
        application/json:
          responses:
            200:
              body:
                application/json: Groups[]
            401:
             body:
                application/json: |
                  {"message": "Erro na operação"}
            404:
             body:
               application/json: |
                 {"message": "Client error"}

/users:
  post:
    description: create user
    securedBy: JWT  
    body:
      application/json:
        properties:
          name: string
          email: string
          password: string
          last_login: datetime
        example:
          {"name": "string",
           "email": "teste@teste.com",
           "password": "string",
           "last_login": "datetime"}
        responses:
          201:
            body:
              application/json: User[]  
            401:
              body:
                application/json: |
                  {"message": "Erro na operação"}

  get: 
    description: get users data
    securedBy: JWT  
    body:
      application/json:
        responses:
          200:
            body:
              application/json: Users[]
          401:
            body:
              type: Erro na operação
  
  /{id}:
    get: 
      description: get user data by id
      securedBy: JWT  
      body:
        application/json:
          responses:
            200:
              body:
                application/json: User
            401:
              body:
                type: Erro na operação

    post:
      description: create user
      securedBy: JWT  
      body:
        application/json:
          responses:
            200:
              body:
                application/json: User
            401:
              body:
                application/json: |
                  {"message": "Erro na operação"}

    delete: 
      description: delete user by id
      securedBy: JWT  
      responses:
        200:
          body:
            application/json: |
              {"message": "User deleted"} 
        401:
          body:
            application/json: |
              {"message": "Operation error"}
        404:
          body:
            application/json: |
              {"message": "Client error"}
  
    put:
      description: update user data by id
      securedBy: JWT  
      body:
        application/json:
          responses:
            200:
              body:
                application/json: User
            401:
              body:
                application/json: |
                  {"message": "Operation error"}
            404:
             body:
               application/json: |
                 {"message": "Client error"}

"""
