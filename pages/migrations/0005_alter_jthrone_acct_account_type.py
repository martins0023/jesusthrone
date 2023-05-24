# Generated by Django 4.0.4 on 2023-05-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_message_alter_jthrone_acct_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jthrone_acct',
            name='account_type',
            field=models.CharField(choices=[('RCCG JESUS THRONE ZONAL ACCOUNT DETAILS', 'RCCG JESUS THRONE ZONAL ACCOUNT DETAILS'), ('RCCG PROJECT ACCOUNT', 'RCCG PROJECT ACCOUNT DETAILS'), ('RCCG JESUS THRONE ACCOUNT DETAILS', 'RCCG JESUS THRONE ACCOUNT DETAILS'), ('OTHERS', 'OTHERS'), ('RCCG JESUS THRONE YOUTH ACCOUNT DETAILS', 'RCCG JESUS THRONE YOUTH ACCOUNT DETAILS')], default='OTHERS', max_length=300),
        ),
    ]