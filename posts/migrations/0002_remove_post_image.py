# Generated by Django 5.1.3 on 2024-11-27 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image",
        ),
    ]
