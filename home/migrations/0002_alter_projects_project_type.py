# Generated by Django 4.0.4 on 2023-03-12 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_type',
            field=models.CharField(choices=[('Regional', 'Regional'), ('Others', 'Others'), ('Provincial', 'Provincial'), ('Zone', 'Zone')], default='Zone', max_length=255),
        ),
    ]