# Generated by Django 4.1.2 on 2022-10-14 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_folio_options_remove_folio_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='type',
        ),
    ]