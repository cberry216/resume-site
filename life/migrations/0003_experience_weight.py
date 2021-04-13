# Generated by Django 2.1.7 on 2019-03-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_experience_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='weight',
            field=models.IntegerField(default=0, help_text='Affects how projects show up; lighter projects appear first, heavier projects last.'),
        ),
    ]
