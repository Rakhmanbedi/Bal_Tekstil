# Generated by Django 4.1.5 on 2023-02-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_update', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
