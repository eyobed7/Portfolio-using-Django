# Generated by Django 5.1.2 on 2024-10-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default='about/eyobed.jpg', upload_to='about'),
        ),
    ]
