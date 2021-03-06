# Generated by Django 2.1.7 on 2019-03-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_education_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='weight',
            field=models.IntegerField(default=0, help_text='Affects how projects show up; lighter projects appear first, heavier projects last.'),
        ),
    ]
