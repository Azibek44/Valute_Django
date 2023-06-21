# Generated by Django 4.2.2 on 2023-06-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_settings_delete_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='logo',
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_dark',
            field=models.ImageField(default=1, upload_to='logo_dark/', verbose_name='Логотип сайта темной темы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_light',
            field=models.ImageField(default=1, upload_to='logo_light/', verbose_name='Логотип  сайта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
    ]
