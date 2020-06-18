from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(["POST"])
def lambda_function(request):
    question = request.data.get("question")
    contador_itens = Counter(question)
    response_list = []
    compare_list = Counter(question).most_common()
    for item in question:
        for x in compare_list:
            if x[0] == item:
                response_list.append(x[1])
    return Response({"solution": response_list})


