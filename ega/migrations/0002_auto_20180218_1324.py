# Generated by Django 2.0.2 on 2018-02-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ega', '0001_squashed_0009_match_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egauser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
