# Generated by Django 4.1.6 on 2023-02-16 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_comment"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="pub_date",),
    ]
