# Generated by Django 4.0.4 on 2023-05-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_projects_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_type',
            field=models.CharField(choices=[('Zone', 'Zone'), ('Regional', 'Regional'), ('Provincial', 'Provincial'), ('Others', 'Others')], default='Zone', max_length=255),
        ),
    ]
