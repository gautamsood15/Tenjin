# Generated by Django 4.1 on 2022-09-04 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("TenjinApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="response",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="TenjinApp.response",
            ),
        ),
    ]
