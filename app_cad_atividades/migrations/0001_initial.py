# Generated by Django 5.0.3 on 2024-04-01 01:55

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Atividade",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("atividade", models.TextField(max_length=255)),
                ("dt_atividade", models.DateField()),
            ],
        ),
    ]
