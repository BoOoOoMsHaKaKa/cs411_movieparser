# Generated by Django 2.1.7 on 2019-04-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190419_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_actors',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_directors',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_movies',
            field=models.CharField(max_length=255, null=True),
        ),
    ]