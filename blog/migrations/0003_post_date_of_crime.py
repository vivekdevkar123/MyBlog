# Generated by Django 4.0.4 on 2022-12-01 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Date_of_crime',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]