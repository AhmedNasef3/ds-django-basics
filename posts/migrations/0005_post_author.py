# Generated by Django 5.1.3 on 2024-11-27 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_author",
                to="posts.author",
            ),
            preserve_default=False,
        ),
    ]
