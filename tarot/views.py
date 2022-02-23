from django.http.response import HttpResponse
from django.template import loader
from .models import Tarot

def homepage(request):
    tarot_generate = Tarot.objects.order_by('?').first()
    template = loader.get_template('home.html')
    context = {'tarot_generate':tarot_generate}
    output = template.render(context)
    return HttpResponse(output)

def meanings(request):
    tarot_list = Tarot.objects.all()
    template = loader.get_template('meanings.html')
    context = {'tarot_list': tarot_list}
    output = template.render(context)
    return HttpResponse(output)


