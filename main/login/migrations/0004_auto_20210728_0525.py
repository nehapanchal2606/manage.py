# Generated by Django 2.0.13 on 2021-07-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210728_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
