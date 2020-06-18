from collections import Counter


request = {"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}

def lambda_function(request):
    question = request['question']
    print('-----', question)
    print('----', counter)
    print('-----', counter_common)

lambda_function(request)
