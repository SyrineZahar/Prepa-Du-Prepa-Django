# Generated by Django 5.0.6 on 2024-05-17 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrepaDuPrepa', '0002_alter_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='desciption',
            new_name='description',
        ),
    ]