from django.http.response import JsonResponse, HttpResponse

def endpointResponse(status_code, massage, data):
    response = {}
    response['status_code'] = status_code
    response['massage'] = massage
    response['data'] = data
    HttpResponse.status_code = status_code
    return JsonResponse(response)