# Generated by Django 4.0.4 on 2023-05-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_projects_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_type',
            field=models.CharField(choices=[('Provincial', 'Provincial'), ('Zone', 'Zone'), ('Others', 'Others'), ('Regional', 'Regional')], default='Zone', max_length=255),
        ),
    ]
