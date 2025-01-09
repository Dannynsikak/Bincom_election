# Generated by Django 5.1.4 on 2025-01-09 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('lga_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('state_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedLGAResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_abbreviation', models.CharField(max_length=255)),
                ('party_score', models.IntegerField()),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.lga')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedPUResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_abbreviation', models.CharField(max_length=255)),
                ('party_score', models.IntegerField()),
                ('polling_unit_uniqueid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.pollingunit')),
            ],
        ),
    ]
