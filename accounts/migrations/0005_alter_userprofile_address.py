# Generated by Django 4.2.3 on 2024-03-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_address1_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]