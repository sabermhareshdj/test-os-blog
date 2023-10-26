# Generated by Django 4.2 on 2023-10-26 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_create_date_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]