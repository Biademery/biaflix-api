# Generated by Django 4.1.7 on 2023-02-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imageURL', models.CharField(max_length=300)),
                ('movieURL', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]