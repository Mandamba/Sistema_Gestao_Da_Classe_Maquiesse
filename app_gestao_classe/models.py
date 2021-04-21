from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, date

now = datetime.now()

# Create your models here.
class UsuarioCustomizado(AbstractUser):
    user_type_data = (
        (1, "AdminPanel"),
        (2, "ModuloGeral"),
        (3, "ModuloCrianca"),
        (4, "ModuloJuvel"),
        (5, "ModuloMulher"),
        (6, "Cultura"),
        (6, "Patrimonio"),
        (7, "Fiscalizacao"),
    )
    user_type = models.CharField(default=1, choices=user_type_data, max_length=15)


class admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    admin = models.OneToOneField(UsuarioCustomizado, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    provincia = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=150)
    provinciaId = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Tribo(models.Model):
    id = models.AutoField(primary_key=True)
    tribo = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=150)
    triboId = models.ForeignKey(Tribo, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class TipoContacto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    contacto = (models.IntegerField(),)
    TipoContactoId = models.ForeignKey(TipoContacto, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class HabilitacaoLiteraria(models.Model):
    id = models.AutoField(primary_key=True)
    habilitacaoLiteraria = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Funcao(models.Model):
    id = models.AutoField(primary_key=True)
    funcao = models.CharField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Bairro(models.Model):
    id = models.AutoField(primary_key=True)
    bairro = models.CharField(max_length=250)
    municipioId = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Rua(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=150)
    numRua = models.CharField(max_length=100)
    bairroId = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    RuaId = models.ForeignKey(Rua, on_delete=models.CASCADE)
    casaNum = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Deficiencia(models.Model):
    id = models.AutoField(primary_key=True)
    deficiencia = models.CharField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class estadoMembro(models.Model):
    id = models.AutoField(primary_key=True)
    estadoId = models.ForeignKey(Estado, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Estrutura(models.Model):
    id = models.AutoField(primary_key=True)
    estrutura = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class EstruturaClasse(models.Model):
    id = models.AutoField(primary_key=True)
    estruturaId = models.ForeignKey(Estrutura, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Membro(models.Model):
    id = models.AutoField(primary_key=True)
    nomeCompleto = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    dataNascimento = models.DateField()
    dataAdmissaoIgreja = models.DateField()
    batizado = models.CharField(max_length=50)
    orfao = models.CharField(max_length=50)
    parteOrfao = models.CharField(max_length=50)
    numeroCartao = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estadoReligioso = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    portadorDeficiencia = models.CharField(max_length=50)
    selecionaAdeficiencia = models.CharField(max_length=50, null=True)
    genero = models.CharField(max_length=10)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    condicaoIndividual = models.CharField(max_length=50, default="Não Aplicável")
    sustento = models.CharField(max_length=50, default="Pais")
    dentroSistemaEnsino = models.CharField(max_length=20, default="Sim")
    ruaId = models.ForeignKey(Rua, on_delete=models.CASCADE, null=True)
    imagem = models.FileField()
    objects = models.Manager()

    def idade(self):
        hoje = date.today()
        return (
            hoje.year
            - self.dataNascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.dataNascimento.month, self.dataNascimento.day)
            )
        )

    def Is_Jovem(self):
        if self.idade() >= 18 and self.idade() <= 35:
            return self
        else:
            return 0

    def jovens_Masculino(self):
        if self.idade() >= 18 and self.idade() <= 35 and self.genero == "Masculino":
            return self
        else:
            return 0

    def jovens_Femenino(self):
        if self.idade() >= 18 and self.idade() <= 35 and self.genero == "Femenino":
            return self
        else:
            return 0

    def IsCrianca(self):
        if self.idade() < 12:
            return self
        else:
            return False

    def IsCriancaMasculino(self):
        if self.idade() < 12 and self.genero == "Masculino":
            return self
        else:
            return False

    def IsCriancaFemenino(self):
        if self.idade() < 12 and self.genero == "Femenino":
            return self
        else:
            return False

    def IsAdolescente(self):
        if self.idade() >= 12 and self.idade() < 18:
            return self
        else:
            return False

    def IsAdolescentesMasculino(self):
        if self.idade() >= 12 and self.idade() <= 17 and self.genero == "Masculino":
            return self
        else:
            return False

    def IsAdolescentesFemenino(self):
        if self.idade() >= 12 and self.idade() <= 17 and self.genero == "Femenino":
            return self
        else:
            return False

    def AllConselhoCrianca(self):
        total = 0
        if self.idade() < 18:
            return self
        else:
            return 0

    def AllMae(self):
        if self.idade() > 36 and self.genero == "Femenino":
            return self
        else:
            return 0

    def AllPai(self):
        if self.idade() > 36 and self.genero == "Masculino":
            return self
        else:
            return 0

    def Is_Deficiente(self):
        if self.portadorDeficiencia == "Sim":
            return self

    def AllOrfao(self):
        if self.orfao == "Sim":
            return self

    def AllRecemConvertidos(self):
        dataAtual = date.today()
        if(self.dataAdmissaoIgreja.year == dataAtual.year):
            return self

    def Is_Casado(self):
        if self.estadoReligioso == "Casado":
            return self

    def Is_Solteiro(self):
        if self.estadoReligioso == "Solteiro":
            return self

    def ViveMaritalmente(self):
        if self.estadoReligioso == "Vivência Marital":
            return self

    def AllViuva(self):
        if self.condicaoIndividual == "Viúva":
            return self

    def TotalViuvos(self):
        if self.condicaoIndividual == "Viúvo":
            return self


class Filiacao(models.Model):
    id = models.AutoField(primary_key=True)
    membroId = models.ForeignKey(Membro, on_delete=models.CASCADE)
    nomePai = models.CharField(max_length=150)
    nomeMae = models.CharField(max_length=150)
    PaiTocoista = models.CharField(max_length=40)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Profissao(models.Model):
    id = models.AutoField(primary_key=True)
    profissao = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class EstadoHabiliatacao(models.Model):
    id = models.AutoField(primary_key=True)
    estadoId = models.ForeignKey(Estado, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class HabilitacaoLiterariaMembro(models.Model):
    id = models.AutoField(primary_key=True)
    habilitacaoLiterariaId = models.ForeignKey(
        HabilitacaoLiteraria, on_delete=models.CASCADE
    )
    cursoId = models.ForeignKey(Curso, on_delete=models.CASCADE)
    membroId = models.ForeignKey(Membro, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    estadoId = models.ForeignKey(Estado, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ProfissaoMembro(models.Model):
    id = models.AutoField(primary_key=True)
    membroId = models.ForeignKey(Membro, on_delete=models.CASCADE)
    profissaoId = models.ForeignKey(Profissao, on_delete=models.CASCADE)
    estadoId = models.ForeignKey(Estado, on_delete=models.CASCADE)
    DesignacaoColectiva = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ContactoMembro(models.Model):
    id = models.AutoField(primary_key=True)
    contactoId = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    membroId = models.ForeignKey(Membro, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Posicao(models.Model):
    id = models.AutoField(primary_key=True)
    posicao = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class EnderecoMembro(models.Model):
    id = models.AutoField(primary_key=True)
    enderecoId = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    membroId = models.ForeignKey(Membro, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class SubEstrutura(models.Model):
    id = models.AutoField(primary_key=True)
    subestrutura = models.CharField(max_length=200)
    estruturaId = models.ForeignKey(Estrutura, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class MembrosSubEstrutura(models.Model):
    id = models.AutoField(primary_key=True)
    membroId = models.ForeignKey(Membro, on_delete=models.CASCADE)
    subEstruturaId = models.ForeignKey(SubEstrutura, on_delete=models.CASCADE)
    funcaoId = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    posicaoId = models.ForeignKey(Posicao, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


@receiver(post_save, sender=UsuarioCustomizado)
def Criar_perfil_Usuario(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Membro.objects.create(admin=instance)
        if instance.user_type == 3:
            Membro.objects.create(admin=instance)
        if instance.user_type == 4:
            Membro.objects.create(admin=instance)
        if instance.user_type == 5:
            Membro.objects.create(admin=instance)
        if instance.user_type == 6:
            Membro.objects.create(admin=instance)
        if instance.user_type == 7:
            Membro.objects.create(admin=instance)


@receiver(post_save, sender=UsuarioCustomizado)
def salvar_perfil_usuario(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.Membro.save()
    if instance.user_type == 3:
        instance.Membro.save()
    if instance.user_type == 4:
        instance.Membro.save()
    if instance.user_type == 5:
        instance.Membro.save()
    if instance.user_type == 6:
        instance.Membro.save()
    if instance.user_type == 7:
        instance.Membro.save()