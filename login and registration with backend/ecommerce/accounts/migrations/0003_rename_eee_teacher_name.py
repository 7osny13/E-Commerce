# Generated by Django 4.0.6 on 2022-07-18 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_name_teacher_eee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='eee',
            new_name='name',
        ),
    ]
