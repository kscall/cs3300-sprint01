# Generated by Django 4.2.7 on 2023-11-02 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0004_remove_review_rating_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]