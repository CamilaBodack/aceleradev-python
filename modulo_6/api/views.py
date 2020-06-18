from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(["POST"])
def lambda_function(request):
    question = request.data.get("question")
    response_list = []
    for numero_lista in Counter(question).most_common():
        for contador in range(0, numero_lista[1]):
            response_list.append(numero_lista[0])
    return Response({"solution": response_list})
