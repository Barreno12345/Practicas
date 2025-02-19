# Generated by Django 5.1.1 on 2024-10-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='photos')),
                ('model', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Personal',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'publicaciones'},
        ),
    ]
