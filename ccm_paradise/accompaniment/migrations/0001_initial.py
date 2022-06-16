# Generated by Django 3.2.13 on 2022-06-16 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('artist', models.CharField(max_length=512)),
                ('lyrics', models.TextField()),
                ('album_cover', models.URLField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Chord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('woman_chord_whether', models.BooleanField()),
                ('man_chord_whether', models.BooleanField()),
                ('youtube_embedded_source', models.CharField(max_length=5012)),
                ('youtube_url', models.URLField(max_length=5012)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chord_music', to='accompaniment.music')),
                ('pitch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chord_pitch', to='accompaniment.pitch')),
            ],
        ),
    ]
