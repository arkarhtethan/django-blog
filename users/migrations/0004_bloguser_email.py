# Generated by Django 2.2 on 2019-05-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_bloguser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
