# Generated by Django 3.0.5 on 2020-06-23 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breedname', models.CharField(max_length=50)),
                ('breedDescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'breeds',
                'db_table': 'breed',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogName', models.CharField(max_length=255)),
                ('dogMass', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('dogEntrydate', models.DateField()),
                ('dogUrl', models.URLField(blank=True, null=True)),
                ('dogDescription', models.TextField()),
                ('dogType', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finalapp.Breed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'dogs',
                'db_table': 'dog',
            },
        ),
        migrations.CreateModel(
            name='DogReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtitle', models.CharField(max_length=255)),
                ('reviewdate', models.DateField()),
                ('reviewrating', models.SmallIntegerField()),
                ('reviewtext', models.TextField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.Dog')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'dogreviews',
                'db_table': 'dogreview',
            },
        ),
    ]
