# Generated by Django 4.0.4 on 2023-05-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_jthrone_acct_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='OurhistoryP2',
            field=models.TextField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='OurhistoryP3',
            field=models.TextField(max_length=40000),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='aboutIntro',
            field=models.CharField(default='Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line', max_length=7000),
        ),
        migrations.AlterField(
            model_name='jthrone_acct',
            name='account_type',
            field=models.CharField(choices=[('OTHERS', 'OTHERS'), ('RCCG JESUS THRONE YOUTH ACCOUNT DETAILS', 'RCCG JESUS THRONE YOUTH ACCOUNT DETAILS'), ('RCCG PROJECT ACCOUNT', 'RCCG PROJECT ACCOUNT DETAILS'), ('RCCG JESUS THRONE ZONAL ACCOUNT DETAILS', 'RCCG JESUS THRONE ZONAL ACCOUNT DETAILS'), ('RCCG JESUS THRONE ACCOUNT DETAILS', 'RCCG JESUS THRONE ACCOUNT DETAILS')], default='OTHERS', max_length=300),
        ),
    ]
