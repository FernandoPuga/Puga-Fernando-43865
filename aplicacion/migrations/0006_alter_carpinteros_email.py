# Generated by Django 4.2.3 on 2023-08-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_rename_cursoemail_carpinteros_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpinteros',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
