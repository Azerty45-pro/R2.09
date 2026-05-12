from django.shortcuts import render
from .forms import LivreForm
from . import models


def ajout(request):

    if request.method == "POST":

        # récupération des données du formulaire
        form = LivreForm(request.POST)

        # validation
        if form.is_valid():

            Livre = form.save()

            return render(
                request,
                "bibliotheque/traitement.html",
                {"Livre": Livre}
            )

        else:

            return render(
                request,
                "bibliotheque/ajout.html",
                {"form": form}
            )

    else:

        # formulaire vide
        form = LivreForm()

        return render(
            request,
            "bibliotheque/ajout.html",
            {"form": form}
        )


def traitement(request):

    lform = LivreForm(request.POST)

    if lform.is_valid():

        Livre = lform.save()

        return render(
            request,
            "bibliotheque/traitement.html",
            {"Livre": Livre}
        )

    else:

        return render(
            request,
            "bibliotheque/ajout.html",
            {"form": lform}
        )