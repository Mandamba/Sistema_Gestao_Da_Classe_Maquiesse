# Generated by Django 3.1.7 on 2021-04-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestao_classe', '0003_membro_sustento'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='dentroSistemaEnsino',
            field=models.CharField(default='Sim', max_length=20),
        ),
    ]
