# Generated by Django 5.1.2 on 2024-10-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0030_remove_resourcerequest_is_approved_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="location",
        ),
        migrations.AddField(
            model_name="profile",
            name="emergency_contact",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
