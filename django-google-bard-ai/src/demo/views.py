from django.shortcuts import render
from .google_bard import get_response
from django.http import JsonResponse

def index(request):
    return render(request, "index.html")


def google_bard_response(request):
    response = get_response(request.GET.get('prompt'))
    if response:
        return JsonResponse({'message': response})
    else:
        return JsonResponse({'message': "I'm sorry, but your question seems to be out of the current context. Let's refocus on topics related to academics. How can I assist you with questions in that area?"})
