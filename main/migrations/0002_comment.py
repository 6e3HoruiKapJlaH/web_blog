# Generated by Django 3.2.4 on 2021-07-23 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Author nickname')),
                ('text', models.TextField(max_length=350, verbose_name='Comment text')),
                ('avatar', models.ImageField(upload_to='images')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
            ],
        ),
    ]
