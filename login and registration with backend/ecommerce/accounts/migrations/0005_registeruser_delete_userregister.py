# Generated by Django 4.0.6 on 2022-07-19 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_teacher_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='userRegister',
        ),
    ]
