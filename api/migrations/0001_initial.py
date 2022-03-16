# Generated by Django 4.0.3 on 2022-03-16 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tunefind_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('tunefind_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('tunefind_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SeriesTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('tunefind_url', models.URLField()),
                ('youtube_url', models.URLField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.episode')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('tunefind_url', models.URLField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.show')),
            ],
        ),
        migrations.CreateModel(
            name='MovieTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('tunefind_url', models.URLField()),
                ('youtube_url', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.season')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.season'),
        ),
    ]
