# Generated by Django 4.1.7 on 2023-03-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Titulo', max_length=200),
            preserve_default=False,
        ),
    ]