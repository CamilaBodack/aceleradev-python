from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from collections import Counter


@api_view(["POST"])
def lambda_function(request):
    question = request.data.get("question")
    if question is None:
        return ValidationError('Question value is empty')
    else:
        lista_response = []
        for numero_lista in Counter(question).most_common():
            for contador in range(0, numero_lista[1]):
                lista_response.append(numero_lista[0])
        return Response({"solution": lista_response})

