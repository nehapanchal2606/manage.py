# Generated by Django 2.0.13 on 2021-07-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20210728_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.FileField(upload_to=''),
        ),
    ]