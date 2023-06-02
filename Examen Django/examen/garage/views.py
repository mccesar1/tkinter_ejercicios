from django.shortcuts import render

from garage.models import Contrato


# Create your views here.
def index(request,):

    contratos = Contrato.objects.all()


    return render(request, 'index.html' , {'contratos': contratos})
