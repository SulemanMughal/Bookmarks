# Generated by Django 4.0.6 on 2022-09-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
