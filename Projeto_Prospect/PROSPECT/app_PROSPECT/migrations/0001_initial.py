# Generated by Django 4.2.4 on 2023-08-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=24)),
                ('email', models.CharField(max_length=120)),
                ('observacao', models.TextField()),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('atualizado_em', models.DateField(auto_now_add=True)),
            ],
        ),
    ]