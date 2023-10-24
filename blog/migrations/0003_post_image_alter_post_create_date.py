# Generated by Django 4.2 on 2023-10-24 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author_post_tags_alter_post_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=' ', upload_to='posts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 16, 15, 39, 684311, tzinfo=datetime.timezone.utc)),
        ),
    ]
