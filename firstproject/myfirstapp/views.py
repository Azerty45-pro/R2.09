from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myfirstapp/home.html')

def index(request):
    return render(request, 'myfirstapp/index.html')

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')

def bonjour(request):
    nom=request.GET["nom"] # récupère la valeur du paramètre nom du formulaire
    return render(request,'myfirstapp/bonjour.html',{"nom":nom}) # passe cette valeur à la vue au travers du dictionnaire de contexte