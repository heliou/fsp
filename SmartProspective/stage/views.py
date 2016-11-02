from django.http import HttpResponse

# Create your views here.
def basic(request):
    return HttpResponse("It's a basic page, in a basic stage")

def variable(request):
    text_variable = "It's a var !"
    return HttpResponse(text_variable)

def default(request):
    return HttpResponse("Default display")
