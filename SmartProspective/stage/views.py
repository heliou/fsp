from django.http import HttpResponse

# Create your views here.
def basic(request):
    return HttpResponse("It's a basic page, in a basic stage")

def variable(request):
    return HttpResponse("It's a VAR page, in a VAR stage")

def default(request):
    return HttpResponse("Default display")
