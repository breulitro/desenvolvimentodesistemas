# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(max_length=9)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('number', models.DecimalField(max_digits=10, decimal_places=0)),
                ('district', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('occupation', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('date_of_birth', models.DateField(null=True)),
                ('nationality', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='patient',
            field=models.OneToOneField(null=True, blank=True, to='medical.Patient'),
        ),
    ]
