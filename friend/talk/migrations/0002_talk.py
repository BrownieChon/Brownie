# Generated by Django 4.0.5 on 2022-06-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
