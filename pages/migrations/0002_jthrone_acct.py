# Generated by Django 4.0.4 on 2023-03-13 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jthrone_acct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(default='RCCG JESUS THRONE ACCOUNT DETAILS', max_length=300)),
                ('account_number', models.CharField(default='2123587356', max_length=300)),
                ('account_bank', models.CharField(default='UBA BANK', max_length=300)),
            ],
        ),
    ]