# Generated by Django 3.1.5 on 2021-01-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='time',
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(max_length=2000),
        ),
    ]
