# Generated by Django 5.2.4 on 2025-07-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_registeruser_username_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
    ]
