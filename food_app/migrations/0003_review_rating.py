# Generated by Django 4.2.7 on 2023-11-02 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
        ('food_app', '0002_alter_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.STAR_RATINGS_RATING_MODEL),
            preserve_default=False,
        ),
    ]
