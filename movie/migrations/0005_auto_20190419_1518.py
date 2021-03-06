# Generated by Django 2.1.7 on 2019-04-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20190419_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='length',
        ),
        migrations.AddField(
            model_name='movies',
            name='averageRating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='numVotes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='runtimeMinutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='genres',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='releaseYear',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
