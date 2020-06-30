
doc = """
title: API Modulo 8
baseUri: http://modulo8.com/{version}
version: v1
mediaType: aplication/json

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token : string
  Agent:
    type: object

/auth/token:
  post: #Solicita um token para API

/agents: #Recursos de agentes
  post: #Cria um agente
  get: #Lista todos agentes
  /{id}:
    delete: #Remove o agente pelo id
    put: #Atualiza os dados do usuario pelo id
  /{id}/events:
    post: #Cria um evento
    get: #Lista o evento
    delete: #Remove o evento pelo id
    put: #Atualiza o evento pelo id
  /{id}/events/{id}:
     post: #Cria um evento
     get: #Lista o evento
     delete: #Remove o evento pelo id
     put: #Atualiza o evento pelo id

/groups: #Recursos de grupos
  post: #Cria um grupo
  get: #Lista todos grupos
  /{id}:
    delete: #Remove um grupo pelo id
    put: #Atualiza o grupo pelo id

/users: #Recursos de usuarios
  post: #Cria um usuario
  get: #Lista todos usuarios
  /{id}:
    delete: #Remove o usuario pelo id
    put: #Atualiza os dados do usuario pelo id


"""
