# Generated by Django 4.0.6 on 2022-07-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist_app', '0002_post_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
