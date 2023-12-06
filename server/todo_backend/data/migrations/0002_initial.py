# Generated by Django 4.2.6 on 2023-12-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_r',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('desc', models.TextField()),
                ('priority', models.CharField(max_length=10)),
                ('user', models.CharField(max_length=10)),
            ],
        ),
    ]
