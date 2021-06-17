# Generated by Django 3.2.3 on 2021-06-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_add_library_ForeignKey'),
    ]

    operations = [
        migrations.AddField(
            model_name='phototag',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phototag',
            name='extra_data',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='phototag',
            name='retrained_model_version',
            field=models.PositiveBigIntegerField(default=0, help_text='If classifier has models that are re-trained locally (e.g. Face) then we want to store this too (YYYYMMDDHHMMSS)'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='flash',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='phototag',
            name='model_version',
            field=models.PositiveIntegerField(default=0, help_text='Version number of classifier model if source is Computer (YYYYMMDD)'),
        ),
    ]
