# Generated by Django 4.0.4 on 2023-05-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Your name', max_length=200)),
                ('email_address', models.EmailField(default='Email address', max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.CharField(choices=[('House Fellowship', 'House Fellowship'), ('Holy Ghost Service', 'Holy Ghost Service'), ('Digging Deep', 'Digging Deep'), ('Talks', 'Talks'), ('Annaual Convention', 'Annaual Convention'), ('Sunday School', 'Sunday School'), ('Motivation', 'Motivation'), ('Faith Clinic', 'Faith Clinic'), ('Anniversary', 'Anniversary'), ('Sunday Sermon', 'Sunday Sermon'), ('Hymns', 'Hymns'), ('Open Heavens', 'Open Heavens'), ('Article', 'Article')], default=None, max_length=300),
        ),
    ]
