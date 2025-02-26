# Generated by Django 5.0.2 on 2024-03-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('date', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=43)),
                ('paragraph', models.TextField(max_length=100)),
            ],
        ),
    ]
