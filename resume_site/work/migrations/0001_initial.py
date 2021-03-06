# Generated by Django 2.1.7 on 2019-03-20 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='work/')),
                ('date_started', models.DateField()),
                ('date_ended', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('website_link', models.CharField(max_length=200)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
