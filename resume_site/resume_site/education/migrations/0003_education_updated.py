# Generated by Django 2.1.7 on 2019-03-22 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_education_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
