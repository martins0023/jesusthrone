# Generated by Django 4.0.4 on 2023-05-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_projects_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_id', models.IntegerField()),
                ('work_process_title', models.CharField(max_length=255)),
                ('work_process_content', models.TextField(max_length=2000)),
                ('work_process_icon', models.CharField(choices=[('hand-shake', 'hand-shake'), ('answer', 'answer'), ('house-1', 'house-1'), ('sketch', 'sketch')], default='hand-shake', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_type',
            field=models.CharField(choices=[('Regional', 'Regional'), ('Zone', 'Zone'), ('Provincial', 'Provincial'), ('Others', 'Others')], default='Zone', max_length=255),
        ),
    ]