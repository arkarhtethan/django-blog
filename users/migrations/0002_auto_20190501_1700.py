# Generated by Django 2.2 on 2019-05-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
