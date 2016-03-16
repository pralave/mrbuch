# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20160305_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='branch',
            field=multiselectfield.db.fields.MultiSelectField(max_length=48, null=True, verbose_name=b'Branch', choices=[(b'Mechanical', b'Mechanical'), (b'BioMedical', b'BioMedical'), (b'Computer', b'Computer'), (b'Civil', b'Civil'), (b'Electronics', b'Electronics')]),
        ),
        migrations.AddField(
            model_name='product',
            name='exam',
            field=multiselectfield.db.fields.MultiSelectField(max_length=21, null=True, verbose_name=b'Exams', choices=[(b'GATE', b'GATE'), (b'CAT/MAT', b'CAT/MAT'), (b'GRE', b'GRE'), (b'GMAT', b'GMAT')]),
        ),
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.CharField(default=b'Pune', max_length=60, null=True, verbose_name=b'University Region', choices=[(b'Gujarat', b'Gujarat'), (b'Pune', b'Pune'), (b'Rajasthan', b'Rajasthan')]),
        ),
        migrations.AddField(
            model_name='product',
            name='technology',
            field=multiselectfield.db.fields.MultiSelectField(max_length=42, null=True, verbose_name=b'Technology', choices=[(b'Programming languages', b'Programming languages'), (b'Electronics', b'Electronics'), (b'Computer', b'Computer')]),
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Year', choices=[(b'1 year', b'1 year'), (b'2 year', b'2 year'), (b'3 year', b'3 year'), (b'4 year', b'4 year'), (b'Post Graduation', b'Post Graduate')]),
        ),
    ]
