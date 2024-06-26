# Generated by Django 4.1.4 on 2024-05-03 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0036_alter_enrollment_user_alter_mentorship_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admin",
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
                ("Full_Name", models.CharField(max_length=20)),
                ("Mobile_no", models.CharField(max_length=10)),
                ("EmailID", models.EmailField(max_length=255)),
                ("DOB", models.DateField(blank=True, null=True)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        default="M",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.admin",
            ),
        ),
        migrations.AlterField(
            model_name="mentorship",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.admin",
            ),
        ),
    ]
