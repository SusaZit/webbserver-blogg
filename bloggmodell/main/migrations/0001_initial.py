# Generated by Django 4.0.1 on 2022-03-23 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
    ]