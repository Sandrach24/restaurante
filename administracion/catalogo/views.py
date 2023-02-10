from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Bienvenidos a la UIDE-LOJA")
    return render(request, 'index.html')