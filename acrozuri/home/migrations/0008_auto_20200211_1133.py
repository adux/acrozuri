# Generated by Django 2.2.5 on 2020-02-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_member_payed_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='payed_period',
        ),
        migrations.AddField(
            model_name='member',
            name='paid_period',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
