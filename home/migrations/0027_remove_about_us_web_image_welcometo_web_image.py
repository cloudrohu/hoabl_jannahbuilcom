# Generated by Django 5.0.1 on 2025-05-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_why_invest_delete_contactmessage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_us',
            name='web_image',
        ),
        migrations.AddField(
            model_name='welcometo',
            name='web_image',
            field=models.ImageField(default=1, upload_to='aboutimage/'),
            preserve_default=False,
        ),
    ]
