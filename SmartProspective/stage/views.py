from django.http import HttpResponse
from stage.models import Person

from django.template import RequestContext
from django.shortcuts import render_to_response

#For aduser
#    Account(login="zouzy", password="totototo", email="fabian.le-maux@epitech.eu", age=19, su=True).save()


# Create your views here.
#def index(request):
#    context = RequestContext(request)
#    context_dict = {'boldmessage': "I am bold font from the context"}
#    return render_to_response('stage/index.html', context_dict, context)

##########################################################################################################################################"
def basic(request):
    return HttpResponse("It's a basic page, in a basic stage")
##########################################################################################################################################"
def database(request):
    context = RequestContext(request)
    all_person_list = Person.objects.all()
    context_dict ={'Person': all_person_list}
    return render_to_response('stage/database.html', context_dict, context)
##########################################################################################################################################"
#SAVE

#def variable(request):
 #   text_variable = "It's a var !"
  #  return HttpResponse(text_variable)

#def dataBase(request)
#context = RequestContext(request)

def default(request):
    return HttpResponse("Default display")
