# Generated by Django 3.0.5 on 2020-06-23 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='breedDescription',
            new_name='breeddescription',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='dogType',
            new_name='dogbreed',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='dogDescription',
            new_name='dogdescription',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='dogEntrydate',
            new_name='dogentrydate',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='dogMass',
            new_name='dogmass',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='dogName',
            new_name='dogname',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='dogUrl',
            new_name='dogurl',
        ),
    ]
