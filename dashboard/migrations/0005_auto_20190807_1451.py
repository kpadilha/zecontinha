# Generated by Django 2.0 on 2019-08-07 14:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190805_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='adf_pvalue',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='ang_coef',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='intercept',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='last_resid',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='n_observ',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='resid_std',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='timestamp_calc',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='zscore',
        ),
        migrations.AddField(
            model_name='pairstats',
            name='model_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='trade',
            name='model_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='pairstats',
            name='pair',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='pairstats',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='adf_pvalue',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='ang_coef',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='intercept',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='last_resid',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='n_observ',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='resid_std',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='timestamp_calc',
        ),
        migrations.RemoveField(
            model_name='pairstats',
            name='zscore',
        ),
    ]