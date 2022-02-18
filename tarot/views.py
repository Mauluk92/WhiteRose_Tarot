from django.template import loader 
from django.http.response import HttpResponse

def homepage(request):
    template = loader.get_template('tarot/templates/home.html')
    return HttpResponse(template)

# Create your views here.
