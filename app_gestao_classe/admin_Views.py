from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from app_gestao_classe.models import (
    Membro,
    Municipio,
    Estado,
    Tribo,
    Provincia,
    Categoria,
    Area,
)
from django.core.files.storage import FileSystemStorage
from django.core import files
from datetime import datetime, date
from django.http import JsonResponse
from xhtml2pdf import pisa
from django.template.loader import get_template


def Jovens(request):
    membros_idades = Membro.objects.filter(dataNascimento__isnull=False)
    Contagem_Tatal_Membros = Membro.objects.all().count()
    membros = []
    somatorio_jovens = 0
    for i in membros_idades:
        if i.Is_Jovem():
            somatorio_jovens = somatorio_jovens + 1
            membros.append(i)
    return render(
        request,
        "admin_templates/Jovens.html",
        {
            "somatorio_jovens": somatorio_jovens,
            "membros": membros,
            "Contagem_Tatal_Membros": Contagem_Tatal_Membros,
        },
    )


def membros(request, id):
    Jovenss = []
    MembrosJ = []
    _Criancas = []
    _Mae = []
    _Pai = []
    _Orfao = []
    _JovensMasculinos = []
    _JovensFemenino = []
    _All_Criancas = []
    _All_Criancas_Femenino = []
    _All_Criancas_Masculino = []
    _All_Adolescentes = []
    _All_Adolescentes_Masculino = []
    _All_Adolescentes_Femenino = []
    _All_Conselho_Crianca = []
    _All_Pai = []
    _All_Mae = []
    _All_Viuva = []
    _All_Orfao = []
    _All_RecemConvertidos = []
    _All_Viuvo = []
    data = datetime.now()
    ano = Membro.objects.all()
    anoAtual = data.year
    municipio = Municipio.objects.all()
    membros = Membro.objects.all()
    data_actual = datetime.now()
    membros_idades = Membro.objects.filter(dataNascimento__isnull=False)
    membros_idades = Membro.objects.filter(dataNascimento__isnull=False)
    jovens = 0
    jovensMasculino = 0
    jovensFemenino = 0
    criancas_total = 0
    criancas_femenino = 0
    criancas_masculino = 0
    adolescentes = 0
    adolescentes_masculino = 0
    adolescentes_femenino = 0
    total_conselho_crianca = 0
    TotalViuva = 0
    TotalViuvo = 0
    TotalOrfao = 0
    papas = 0
    mamas = 0
    AllRecemConvertidos = 0
    for p in membros_idades:
        if p.Is_Jovem():
            jovens = jovens + 1
        if p.jovens_Masculino():
            jovensMasculino = jovensMasculino + 1
            _JovensMasculinos.append(p)
        if p.jovens_Femenino():
            jovensFemenino = jovensFemenino + 1
            _JovensFemenino.append(p)
        if p.IsCrianca():
            criancas_total = criancas_total + 1
            _All_Criancas.append(p)
        if p.IsCriancaFemenino() and p.IsCrianca():
            criancas_femenino = criancas_femenino + 1
            _All_Criancas_Femenino.append(p)
        if p.IsCrianca() and p.IsCriancaMasculino():
            criancas_masculino = criancas_masculino + 1
            _All_Criancas_Masculino.append(p)
        if p.IsAdolescente():
            adolescentes = adolescentes + 1
            _All_Adolescentes.append(p)
        if p.IsAdolescentesMasculino():
            adolescentes_masculino = adolescentes_masculino + 1
            _All_Adolescentes_Masculino.append(p)
        if p.IsCriancaFemenino() and p.IsCrianca():
            criancas_femenino = criancas_femenino
        if p.IsAdolescente() and p.IsAdolescentesFemenino():
            adolescentes_femenino = adolescentes_femenino + 1
            _All_Adolescentes_Femenino.append(p)
        if p.AllConselhoCrianca():
            total_conselho_crianca = total_conselho_crianca + 1
            _All_Conselho_Crianca.append(p)
        if p.AllPai():
            papas = papas + 1
            _All_Pai.append(p)
        if p.AllMae():
            mamas = mamas + 1
            _All_Mae.append(p)
        if p.Is_Jovem():
            Jovenss.append(p)
        if p.AllOrfao():
            TotalOrfao = TotalOrfao + 1
            _Orfao.append(p)
            _All_Orfao.append(p)
        if p.AllPai():
            _Pai.append(p)
        if p.AllMae():
            _Mae.append(p)
        if p.IsCrianca():
            _Criancas.append(p)
        if p.AllViuva():
            TotalViuva = TotalViuva + 1
            _All_Viuva.append(p)
        if p.AllRecemConvertidos():
            AllRecemConvertidos = AllRecemConvertidos + 1
            _All_RecemConvertidos.append(p)
        if p.TotalViuvos():
            _All_Viuvo.append(p)
            TotalViuvo = TotalViuvo + 1
    if id == "000":
        MembrosJ = membros
    if id == "001":
        MembrosJ = Jovenss
    if id == "002":
        MembrosJ = _Criancas
    if id == "003":
        MembrosJ = _Mae
    if id == "004":
        MembrosJ = _Pae
    if id == "005":
        MembrosJ = _JovensMasculinos
    if id == "006":
        MembrosJ = _JovensFemenino
    if id == "007":
        MembrosJ = _All_Criancas
    if id == "008":
        MembrosJ = _All_Criancas_Femenino
    if id == "009":
        MembrosJ = _All_Criancas_Masculino
    if id == "010":
        MembrosJ = _All_Adolescentes
    if id == "011":
        MembrosJ = _All_Adolescentes_Masculino
    if id == "012":
        MembrosJ = _All_Adolescentes_Femenino
    if id == "013":
        MembrosJ = _All_Conselho_Crianca
    if id == "014":
        MembrosJ = _All_Pai
    if id == "015":
        MembrosJ = _All_Mae
    if id == "016":
        MembrosJ = _All_Viuva
    if id == "017":
        MembrosJ = _All_Orfao
    if id == "018":
        MembrosJ = _All_RecemConvertidos
    if id == "019":
        MembrosJ = _All_Viuvo
    return render(
        request,
        "admin_templates/membros.html",
        {
            "membros": MembrosJ,
            "municipios": municipio,
            "total": membros.count(),
            "data": data_actual,
            "jovens": jovens,
            "jovensMasculino": jovensMasculino,
            "jovensFemenino": jovensFemenino,
            "criancas_total": criancas_total,
            "criancas_femenino": criancas_femenino,
            "criancas_masculino": criancas_masculino,
            "adolescentes": adolescentes,
            "adolescentes_masculino": adolescentes_masculino,
            "adolescentes_femenino": adolescentes_femenino,
            "total_conselho_crianca": total_conselho_crianca,
            "TotalViuvo": TotalViuvo,
            "papas": papas,
            "TotalViuva": TotalViuva,
            "mamas": mamas,
            "TotalOrfao": TotalOrfao,
            "AllRecemConvertidos": AllRecemConvertidos,
            "id": id,
        },
    )


def admin_home(request):
    return render(request, "admin_templates/home_content.html")


def add_membro(request):
    provincia = Provincia.objects.all()
    municipio = Municipio.objects.all()
    area = Area.objects.all()
    tribo = Tribo.objects.all()
    categoria = Categoria.objects.all()
    estado = Estado.objects.all()
    return render(
        request,
        "admin_templates/add_membro.html",
        {
            "provincia": provincia,
            "area": area,
            "tribo": tribo,
            "categoria": categoria,
            "estado": estado,
            "municipios": municipio,
        },
    )


def add_membro_save(request):

    if request.method != "POST":
        return HttpResponse("Este método não é permitido")

    else:

        nomeCompleto = request.POST.get("nomeCompleto")
        municipioId = request.POST.get("municipio")
        municipio = Municipio.objects.get(id=municipioId)
        dataNascimento = request.POST.get("dataNascimento")
        dataAdmissaoIgreja = request.POST.get("dataAdmissaoIgreja")
        batizado = request.POST.get("batizado")
        databatismo = request.POST.get("databatismo")
        sustento = request.POST.get("sustento")
        orfao = request.POST.get("orfao")
        parteOrfao = request.POST.get("parteOrfao")
        numeroCartao = request.POST.get("numeroCartao")
        categoriaId = request.POST.get("categoria")
        categoria = Categoria.objects.get(id=categoriaId)
        estadoReligioso = request.POST.get("estadoReligioso")
        areaId = request.POST.get("area")
        area = Area.objects.get(id=areaId)
        portadorDeficiencia = request.POST.get("portadorDeficiencia")
        selecionaAdeficiencia = request.POST.get("selecionaAdeficiencia")
        genero = request.POST.get("genero")
        estadoId = request.POST.get("estado")
        estado = Estado.objects.get(id=estadoId)
        condicaoIndividual = request.POST.get("condicaoIndividual")
        NoSistemaEnsino = request.POST.get("NoSistemaEnsino")
        profile_pic = request.FILES["profile_pic"]
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        data_nascimento = datetime.strptime(dataNascimento, "%m/%d/%Y").date()
        data_adimissaoIgreja = datetime.strptime(dataAdmissaoIgreja, "%m/%d/%Y").date()
        print(str(data_nascimento.year))

        try:
            membro = Membro(
                nomeCompleto=nomeCompleto,
                municipio=municipio,
                dataNascimento=data_nascimento,
                dataAdmissaoIgreja=data_adimissaoIgreja,
                batizado=batizado,
                orfao=orfao,
                parteOrfao=parteOrfao,
                numeroCartao=numeroCartao,
                categoria=categoria,
                estadoReligioso=estadoReligioso,
                area=area,
                portadorDeficiencia=portadorDeficiencia,
                selecionaAdeficiencia=selecionaAdeficiencia,
                sustento=sustento,
                condicaoIndividual=condicaoIndividual,
                dentroSistemaEnsino=NoSistemaEnsino,
                genero=genero,
                estado=estado,
                imagem=profile_pic_url,
            )
            membro.save()
            messages.success(request, "Membro Cadastrado com sucesso")
            return HttpResponseRedirect("/add_membro")
        except Exception as e:
            print(e)
            messages.error(
                request,
                "Erro ao cadastrar o membro, verifica os dados e tente novamente!",
            )
            return HttpResponseRedirect("/add_membro")


def add_tribo(request):
    return render(request, "formularios/add_tribo.html")


def add_tribo_save(request):
    if request.method != "POST":
        return HttpResponse(request, "Método inválido")
    else:

        if request.POST.get("tribo") == "":
            messages.warning(request, "O Campo não pode está vazio, preecnha Porfavor!")
            return HttpResponseRedirect("/add_tribo")
        else:
            tribo = request.POST.get("tribo")
            try:
                tribo_model = Tribo(tribo=tribo)
                tribo_model.save()
                messages.success(request, "Cadastro feito com sucesso")
                return HttpResponseRedirect("add_tribo")
            except:
                messages.error(request, "Algo correu mal, verifica e tente novamente!")
                return HttpResponseRedirect("/add_tribo")


def add_provincia(request):

    return render(request, "formularios/add_provincia.html")


def add_provincia_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(request, "Método inválido")
    else:

        if request.POST.get("provincia") == "":
            messages.warning(request, "O Campo não pode está vazio, preecnha Porfavor!")
            return HttpResponseRedirect("/add_provincia")
        else:
            provincia = request.POST.get("provincia")
            try:
                tribo_model = Provincia(provincia=provincia)
                tribo_model.save()
                messages.success(request, "Cadastro feito com sucesso")
                return HttpResponseRedirect("add_provincia")
            except:
                messages.error(request, "Algo correu mal, verifica e tente novamente!")
                return HttpResponseRedirect("/add_provincia")


def add_municipio(request):
    provincia = Provincia.objects.all()
    return render(request, "formularios/add_municipio.html", {"provincia": provincia})


def add_municipio_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(request, "Método inválido")
    else:
        provinciaId = request.POST.get("provincia")
        provincia = Provincia.objects.get(id=provinciaId)
        municipio = request.POST.get("municipio")
        try:
            munipio = Municipio(municipio=municipio, provinciaId=provincia)
            munipio.save()
            messages.success(request, "Municipio Cadastrado com Sucesso")
            return HttpResponseRedirect("add_municipio")
        except:
            messages.error(request, "Algo correu mal, verifica e tente novamente!")
            return HttpResponseRedirect("/add_municipio")


def add_area(request):
    tribo = Tribo.objects.all()
    return render(request, "formularios/add_area.html", {"tribo": tribo})


def add_area_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(request, "Método inválido")
    else:

        triboId = request.POST.get("tribo")
        tribo = Tribo.objects.get(id=triboId)
        area = request.POST.get("area")
        try:
            area = Area(area=area, triboId=tribo)
            area.save()
            messages.success(request, "Área Cadastrado com Sucesso")
            return HttpResponseRedirect("/add_area")
        except:
            messages.error(request, "Algo correu mal, verifica e tente novamente!")
            return HttpResponseRedirect("/add_area")


def add_municipio(request):
    provincia = Provincia.objects.all()
    return render(request, "formularios/add_municipio.html", {"provincia": provincia})


def add_municipio_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(request, "Método inválido")
    else:

        provinciaId = request.POST.get("provincia")
        provincia = Provincia.objects.get(id=provinciaId)
        municipio = request.POST.get("municipio")
        try:
            munipio = Municipio(municipio=municipio, provinciaId=provincia)
            munipio.save()
            messages.success(request, "Municipio Cadastrado com Sucesso")
            return HttpResponseRedirect("add_municipio")
        except:
            messages.error(request, "Algo correu mal, verifica e tente novamente!")
            return HttpResponseRedirect("/add_municipio")


def add_Categoria(request):
    return render(request, "formularios/add_Categoria.html")


def add_Categoria_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(request, "Método inválido")
    else:

        categoria = request.POST.get("categoria")
        try:
            categoria = Categoria(categoria=categoria)
            categoria.save()
            messages.success(request, "Categoria Cadastrado com Sucesso")
            return HttpResponseRedirect("add_Categoria")
        except:
            messages.error(request, "Algo correu mal, verifica e tente novamente!")
            return HttpResponseRedirect("/add_Categoria")


def add_estado(request):
    return render(request, "formularios/add_estado.html")


def add_estado_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(request, "Método inválido")
    else:

        estado = request.POST.get("estado")
        try:
            estado = Estado(estado=estado)
            estado.save()
            messages.success(request, "Estado Cadastrado com Sucesso")
            return HttpResponseRedirect("add_estado")
        except:
            messages.error(request, "Algo correu mal, verifica e tente novamente!")
            return HttpResponseRedirect("/add_estado")


def add_filiacao(request):
    membros = Membro.objects.all()
    return render(request, "formularios/add_filiacao.html", {"membros": membros})


def deletarMembro(request, id):
    get_membro = Membro.objects.get(id=id)
    get_membro.delete()
    return HttpResponseRedirect("/membros/000")


def editar_membro(request, id):
    membro = Membro.objects.get(id=id)
    return render(request, "formularios/editar_membro.html", {"membro": membro})


def detalhe_membro(request, id):
    membro = Membro.objects.get(id=id)
    return render(request, "formularios/detalhe_membro.html", {"membro": membro})


def get_provincias_json(request):
    provincias = list(Provincia.objects.values())
    return JsonResponse({"provincia": provincias})


def get_municipio_json(request):
    municipio = list(Municipio.objects.values())
    return JsonResponse({"municipios": municipio})

def get_tribo(request):
    tribos = list(Tribo.objects.values())
    return JsonResponse({"tribos": tribos})

def get_areas(request):
    areas = list(Area.objects.values())
    return JsonResponse({"areas": areas})


def add_actividade(request):
    return render(request, "formularios/add_actividade.html")


def listagem_criancas(request):
    membros = Membro.objects.filter(dataNascimento__isnull=False)
    conselho_crianca = []
    total_conselho_crianca = 0
    crianca_total = 0
    adolescentes = 0
    criancasMasculino = 0
    criancasFemenino = 0
    orfaos = 0
    adolescentesMasculinos = 0
    adolescentesFemenino = 0
    for i in membros:
        if i.IsCrianca() or i.IsAdolescente():
            total_conselho_crianca = total_conselho_crianca + 1
            conselho_crianca.append(i)
        if i.IsCrianca():
            crianca_total = crianca_total + 1
        if i.IsAdolescente():
            adolescentes = adolescentes + 1
        if i.IsCrianca() and i.IsCriancaMasculino():
            criancasMasculino = criancasMasculino + 1
        if i.IsCriancaFemenino() and i.IsCrianca():
            criancasFemenino = criancasFemenino + 1
        if i.AllOrfao() and i.AllConselhoCrianca():
            orfaos = orfaos + 1
        if i.IsAdolescentesMasculino() and i.IsAdolescente():
            adolescentesMasculinos = adolescentesMasculinos + 1
        if i.IsAdolescentesFemenino() and i.IsAdolescente():
            adolescentesFemenino = adolescentesFemenino + 1
    return render(
        request,
        "listagem_membros/listagem_criancas.html",
        {
            "total": total_conselho_crianca,
            "conselho_crianca": conselho_crianca,
            "crianca_total": crianca_total,
            "adolescentes": adolescentes,
            "criancas_Masculino": criancasMasculino,
            "criancasFemenino": criancasFemenino,
            "orfaos": orfaos,
            "adolescentesMasculinos": adolescentesMasculinos,
            "adolescentesFemenino": adolescentesFemenino,
        },
    )


def conselho_mulher(request):
    membros = Membro.objects.filter(dataNascimento__isnull=False)
    maes = []
    casadas_total = 0
    totalViuvas = 0
    total = 0
    solteiras = 0
    vivemMaritalmenteTotal = 0
    for i in membros:
        if i.AllMae():
            maes.append(i)
            total = total + 1
        if i.AllMae() and i.Is_Casado():
            casadas_total = casadas_total + 1
        if i.AllMae() and i.Is_Solteiro():
            solteiras = solteiras + 1
        if i.AllMae() and i.ViveMaritalmente():
            vivemMaritalmenteTotal = vivemMaritalmenteTotal + 1
        if i.AllViuva and i.AllMae():
            totalViuvas = totalViuvas + 1

    return render(
        request,
        "listagem_membros/conselho_mulher.html",
        {
            "total": total,
            "totalViuvas": totalViuvas,
            "crianca": maes,
            "casadas_total": casadas_total,
            "solteiras": solteiras,
            "vivemMaritalmenteTotal": vivemMaritalmenteTotal,
        },
    )


def render_pdf_view(request):
    template_path = "admin_templates/pdf.html"
    context = {"myvar": "this is your template context"}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response