# Generated by Django 3.2.13 on 2022-06-16 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accompaniment', '0002_auto_20220616_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chord',
            name='pitch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chord_pitch', to='accompaniment.pitch'),
        ),
    ]
