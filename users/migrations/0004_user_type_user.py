# Generated by Django 4.0.6 on 2022-10-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type_user',
            field=models.CharField(default='', max_length=45),
        ),
    ]