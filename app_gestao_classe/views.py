from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from app_gestao_classe.EmailBackend import EmailBackend
from django.contrib import messages

# Create your views here.


def ShowPaginaInicial(request):
    return render(request, "paginaPrincipal.html")


def PaginaLogin(request):
    return render(request, "paginaLogin.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h3>Método não permitido</h3>")
    else:

        user = EmailBackend.authenticate(
            request,
            username=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        if user != None:
            login(request, user)
            return HttpResponseRedirect("paginaPrincipal")

        if request.POST.get("email") == "" or request.POST.get("password") == "":
            messages.warning(request, "Deves Prencher todos campos ilustre, porfavor!")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Dados inválidos, Verifique e tente novamente!")
            return HttpResponseRedirect("/")


def get_user_detail(request):
    if request.user != None:
        return HttpResponse(
            "User: "
            + str(request.user.email)
            + "user_type: "
            + str(request.user.user_type)
        )
    else:
        return HttpResponse("Porfavor faça o login")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


# def add_membro(request):
# return render("templates/membro.html")
