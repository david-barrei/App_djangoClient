# Generated by Django 4.2.5 on 2023-09-12 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='lenguaje')),
            ],
        ),
        migrations.CreateModel(
            name='SO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_so', models.CharField(max_length=100, verbose_name='SO')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ap', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('am', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('foto', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Foto')),
                ('lenguaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.lenguaje', verbose_name='Lenguaje')),
                ('so', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.so', verbose_name='lenguaje')),
            ],
        ),
    ]
