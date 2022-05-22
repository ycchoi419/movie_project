# Generated by Django 3.2.12 on 2022-05-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres_string',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_count',
            field=models.IntegerField(null=True),
        ),
    ]
