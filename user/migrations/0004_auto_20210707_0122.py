# Generated by Django 3.2.5 on 2021-07-07 08:22

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_auto_20210706_2104'),
        ('user', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='country', chained_model_field='country', default=1, on_delete=django.db.models.deletion.CASCADE, to='cities_light.region'),
            preserve_default=False,
        ),
    ]
