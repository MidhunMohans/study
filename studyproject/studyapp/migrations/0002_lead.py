# Generated by Django 3.2.14 on 2022-08-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='pics1')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
