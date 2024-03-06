# Generated by Django 4.2 on 2023-11-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_user_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(blank=True, null=True, to="blog.tag"),
        ),
    ]
