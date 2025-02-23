# Generated by Django 5.1.2 on 2024-10-28 01:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_horta', '0005_horta_comunitaria_horta_participantes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('aprovado', models.BooleanField(default=None, null=True)),
                ('horta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_horta.horta')),
                ('usuario_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
