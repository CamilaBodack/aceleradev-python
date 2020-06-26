import requests
import json
import hashlib
import string
import os


def request_to_codenation():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?'
    token = 'token'
    codenation_url = url + token
    request_to_codenation = requests.get(codenation_url)
    response = request_to_codenation.json()
    with open("answear.json", "w") as json_file:
        json.dump(response, json_file)


request_to_codenation()


def get_data():
    if not os.path.exists('answear.json'):
        request_to_codenation()
    else:
        get_file = open("answear.json")
        data = json.load(get_file)
    return data


def split():
    request_to_codenation()
    data = get_data()
    phrase = data["cifrado"]
    return list(phrase)


def decypher():
    decypher = ""
    alphabet = list(string.ascii_lowercase)
    data = get_data()
    numero_casas = data['numero_casas']
    for letter in split():
        if len(letter.strip()) > 0:
            if letter in alphabet:
                posicao = alphabet.index(letter)
                posicao = posicao - numero_casas
                decypher = decypher + alphabet[posicao]
            else:
                decypher = decypher + letter
        else:
            decypher = decypher + (" ")

    return decypher


def update_decifrado():
    data = get_data()
    data['decifrado'] = decypher()
    with open('answear.json', 'w') as json_file:
        json.dump(data, json_file)


def update_resumo():
    data = get_data()
    message = decypher().encode()
    resumo_criptografico = hashlib.sha1(message)
    data['resumo_criptografico'] = resumo_criptografico.hexdigest()
    with open('answear.json', 'w') as json_file:
        json.dump(data, json_file)


def send_answear():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token'
    result = requests.post(url, files={"answer": open("answear.json", "rb")})
    result.status_code


update_decifrado()
update_resumo()
send_answear()
