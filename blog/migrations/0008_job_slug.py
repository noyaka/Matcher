# Generated by Django 4.0.6 on 2022-07-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='d', max_length=100),
            preserve_default=False,
        ),
    ]
