# Generated by Django 5.0.2 on 2024-02-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_projects_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
    ]
