# Generated by Django 5.1.1 on 2024-09-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('period', models.CharField(max_length=100)),
                ('Skills', models.ManyToManyField(to='content.skill')),
            ],
        ),
    ]
