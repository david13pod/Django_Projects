# Generated by Django 3.1.6 on 2021-06-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('est_app', '0004_property_picture1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='picture1',
        ),
        migrations.AlterField(
            model_name='agent',
            name='pix',
            field=models.ImageField(max_length=500, upload_to='agent_pix/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='picture',
            field=models.ImageField(max_length=500, upload_to='prop_pix/'),
        ),
    ]
