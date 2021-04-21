"""sistema_gestao_classe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from app_gestao_classe import views, admin_Views
from sistema_gestao_classe import settings

urlpatterns = (
    [
        path("paginaPrincipal", views.ShowPaginaInicial, name="paginaPrincipal"),
        path("admin/", admin.site.urls),
        path("", views.PaginaLogin),
        path("doLogin", views.doLogin, name="doLogin"),
        path("get_user_detail", views.get_user_detail),
        path("membros/<str:id>", admin_Views.membros, name="membros"),
        path("add_actividade", admin_Views.add_actividade, name="add_actividade"),
        path("Jovens", admin_Views.Jovens, name="Jovens"),
        path("admin_home", admin_Views.admin_home, name="admin_home"),
        path("add_filiacao", admin_Views.add_filiacao, name="add_filiacao"),
        path("add_membro", admin_Views.add_membro, name="add_membro"),
        path("add_membro_save", admin_Views.add_membro_save),
        path("logout_user", views.logout_user, name="logout_user"),
        path("add_tribo", admin_Views.add_tribo, name="add_tribo"),
        path("add_area", admin_Views.add_area, name="add_area"),
        path("add_area_save", admin_Views.add_area_save, name="add_area_save"),
        path(
            "add_provincia_save", admin_Views.add_provincia_save, name="add_area_save"
        ),
        path("add_provincia", admin_Views.add_provincia, name="add_provincia"),
        path("add_municipio", admin_Views.add_municipio, name="add_municipio"),
        path("add_Categoria", admin_Views.add_Categoria, name="add_Categoria"),
        path(
            "add_Categoria_save",
            admin_Views.add_Categoria_save,
            name="add_Categoria_save",
        ),
        path(
            "add_municipio_save",
            admin_Views.add_municipio_save,
            name="add_municipio_save",
        ),
        path("add_estado", admin_Views.add_estado, name="add_estado"),
        path("add_estado_save", admin_Views.add_estado_save, name="add_estado_save"),
        path("add_tribo_save", admin_Views.add_tribo_save, name="add_tribo_save"),
        path("editar_membro/<str:id>", admin_Views.editar_membro, name="editar_membro"),
        path(
            "get_provincias_json",
            admin_Views.get_provincias_json,
            name="get_provincias_json",
        ),
        path(
            "get_municipio_json",
            admin_Views.get_municipio_json,
            name="get_municipio_json",
        ),
        path(
            "get_tribo",
            admin_Views.get_tribo,
            name="get_tribo",
        ),
        path(
            "get_areas",
            admin_Views.get_areas,
            name="get_areas",
        ),
        path("deletarMembro/<str:id>", admin_Views.deletarMembro, name="deletarMembro"),
        path(
            "detalhe_membro/<str:id>", admin_Views.detalhe_membro, name="detalhe_membro"
        ),
        path(
            "listagem_criancas",
            admin_Views.listagem_criancas,
            name="listagem_criancas",
        ),
        path("conselho_mulher", admin_Views.conselho_mulher, name="conselho_mulher"),
        path("render_pdf_view", admin_Views.render_pdf_view, "render_pdf_view")
        # path('add_membro', ShowPaginaInicial.add_membro)
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
