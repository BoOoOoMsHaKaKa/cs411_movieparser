# Generated by Django 2.1.7 on 2019-04-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
        ('comment', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie_commented',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Movies'),
        ),
    ]