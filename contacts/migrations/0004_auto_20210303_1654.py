# Generated by Django 3.1.5 on 2021-03-03 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20210301_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.category'),
        ),
    ]