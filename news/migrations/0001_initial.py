# Generated by Django 5.1.2 on 2024-10-30 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
