# Generated by Django 4.0.4 on 2023-03-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.CharField(choices=[('House Fellowship', 'House Fellowship'), ('Anniversary', 'Anniversary'), ('Article', 'Article'), ('Sunday School', 'Sunday School'), ('Holy Ghost Service', 'Holy Ghost Service'), ('Motivation', 'Motivation'), ('Faith Clinic', 'Faith Clinic'), ('Hymns', 'Hymns'), ('Digging Deep', 'Digging Deep'), ('Sunday Sermon', 'Sunday Sermon'), ('Annaual Convention', 'Annaual Convention'), ('Open Heavens', 'Open Heavens'), ('Talks', 'Talks')], default=None, max_length=300),
        ),
    ]
