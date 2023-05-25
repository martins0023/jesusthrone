# Generated by Django 4.0.4 on 2023-05-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_blog_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.CharField(choices=[('Hymns', 'Hymns'), ('Sunday School', 'Sunday School'), ('Anniversary', 'Anniversary'), ('Digging Deep', 'Digging Deep'), ('Faith Clinic', 'Faith Clinic'), ('Talks', 'Talks'), ('Open Heavens', 'Open Heavens'), ('House Fellowship', 'House Fellowship'), ('Holy Ghost Service', 'Holy Ghost Service'), ('Article', 'Article'), ('Sunday Sermon', 'Sunday Sermon'), ('Annaual Convention', 'Annaual Convention'), ('Motivation', 'Motivation')], default=None, max_length=300),
        ),
    ]