# Generated by Django 3.0.8 on 2020-08-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
