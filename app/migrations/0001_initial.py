# Generated by Django 4.0.6 on 2022-09-21 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='negocios')),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
                ('tipo_Negocio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_negocio')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('nuevo', models.BooleanField()),
                ('imagen', models.ImageField(null=True, upload_to='negocios/items')),
                ('negocio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_negocio')),
            ],
        ),
    ]
