# Generated by Django 4.2.4 on 2023-08-04 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publicationmodel_likes_count_like_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]