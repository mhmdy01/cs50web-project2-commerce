# Generated by Django 3.2.8 on 2021-10-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_watchlist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
    ]