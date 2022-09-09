# Generated by Django 4.0.4 on 2022-06-19 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_app', '0005_alter_project_client_alter_project_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_app', to=settings.AUTH_USER_MODEL),
        ),
    ]