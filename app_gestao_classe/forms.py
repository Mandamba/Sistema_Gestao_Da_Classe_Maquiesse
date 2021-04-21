from django import forms
from app_gestao_classe.models import Tribo,Area, Municipio, Provincia, Estado, Categoria

class AddMembroForm(forms.Form):
    nomeCompleto = forms.CharField(label="Nome Completo", max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}) )
    provincias = Provincia.objects.all()
    lista_provincia = []
    for provincia in provincias:
        provincia2 = (provincia.id, provincia.provincia)
        lista_provincia.append(provincia2)
    provincia = forms.ChoiceField(label="Seleciona a Província", choices=lista_provincia, widget=forms.Select(attrs={"class":"form-control select2"}))

    municipios = Municipio.objects.all()
    lista_municipio = []

    for municipio in municipios:
        municipio2 = (municipio.id, municipio.municipio)
        lista_municipio.append(municipio2)

    municipio = forms.ChoiceField(label="Seleciona o Município", choices = lista_municipio, widget=forms.Select(attrs={"class":"form-control select2"}))
    dataNascimento = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(attrs={"class":"form-control"}))
    orfaos = (
        ("Sim","Sim"),
        ("Não","Não")
    )
    orfao = forms.ChoiceField(label="Orfão", choices=orfaos, widget=forms.Select(attrs={"class":"form-control select2"}))

    parte_orfao =(
        ("Pai","Pai"),
        ("Mae","Mãe"),
        ("PaiMae","Pai e Mae")
    )
    parteOrfao = forms.ChoiceField(label="Parte de que é orfão", choices=parte_orfao, widget=forms.Select(attrs={"class":"form-control select2"}))
    numeroCartao = forms.CharField(label="Número do Cartão de Membro", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    categorias = Categoria.objects.all()
    lista_categoria = []

    for categoria in categorias:
        categoria = (categoria.id, categoria.categoria)
        lista_categoria.append(categoria)
    categoria = forms.ChoiceField(label="Categoria", choices=lista_categoria, widget=forms.Select(attrs={"class":"form-control select2"}))

    estados_religioso =(
        ("Casado","Casado"),
        ("Solteiro", "Solteiro"),
        ("Vivência marital", "Vivência marital")
    )
    estadoReligioso = forms.ChoiceField(label="Estado Religioso", choices=estados_religioso, widget=forms.Select(attrs={"class":"form-control select2"}))
    
    tribos = Tribo.objects.all()
    lista_tribo = []
    for tribo in tribos:
        tribo = (tribo.id, tribo.tribo)
        lista_tribo.append(tribo)

    tribo = forms.ChoiceField(label="Tribo", choices=lista_tribo, widget=forms.Select(attrs={"class":"form-control select2"}))
    areas = Area.objects.all()
    lista_area = []
    for area in areas:
        area = (area.id, area.area)
        lista_area.append(area)

    area = forms.ChoiceField(label="Área", choices=lista_area, widget=forms.Select(attrs={"class":"form-control select2"}))
    portadorDeficiencia = (
        ("Sim","Sim"),
        ("Não","Não")
    )
    portadorDeficiencia = forms.ChoiceField(label="Portador de Alguma doença", choices=portadorDeficiencia, widget=forms.Select(attrs={"class":"form-control select2"}))
    deficiencias=(("Múltipla","Múltipla"),("Física","Física"),("Visual","Visual"),("Mental","Mental"),("Reablitado","Reablitado"))
    selecionaAdeficiencia = forms.ChoiceField(label="Seleciona a deficiencia", choices=deficiencias, widget=forms.Select(attrs={"class":"form-control select2"}))
    escolha_genero = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino")
    )
    genero = forms.ChoiceField(label="Gênero", choices=escolha_genero, widget=forms.Select(attrs={"class":"form-control select2"}))
    estados = Estado.objects.all()
    lista_estado = []
    for estado in estados:
        estado = (estado.id, estado.estado)
        lista_estado.append(estado)

    estado = forms.ChoiceField(label="Estado do Membro",choices=lista_estado, widget=forms.Select(attrs={"class":"form-control select2"}))
    filePicture = forms.FileField(label="Seleciona uma fotografia", max_length=150)
