# Generated by Django 4.2.7 on 2023-12-10 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='email_confirmation_code',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Email Confirmation Code'),
        ),
        migrations.AlterField(
            model_name='emailconfirmation',
            name='code',
            field=models.CharField(max_length=6, unique=True, verbose_name='Confirmation Code'),
        ),
    ]