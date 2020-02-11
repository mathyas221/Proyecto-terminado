# Generated by Django 2.2 on 2019-11-23 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0021_auto_20191122_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='acquisition',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PostAcquisition', to='propiedades2.Acquisition'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PostRent', to='propiedades2.Rent'),
        ),
    ]
