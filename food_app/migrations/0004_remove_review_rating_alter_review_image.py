# Generated by Django 4.2.7 on 2023-11-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0003_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
