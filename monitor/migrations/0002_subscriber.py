# Generated by Django 2.2.7 on 2019-12-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]