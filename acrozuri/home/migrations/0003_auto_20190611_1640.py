# Generated by Django 2.2.1 on 2019-06-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190611_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=36)),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=72)),
                ('price', models.CharField(max_length=36)),
                ('web', models.CharField(max_length=72)),
                ('note', models.CharField(max_length=144)),
            ],
        ),
        migrations.RenameModel(
            old_name='NewsForm',
            new_name='News',
        ),
    ]