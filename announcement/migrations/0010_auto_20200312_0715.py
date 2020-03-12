# Generated by Django 3.0.3 on 2020-03-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0009_auto_20200312_0601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-updated_at', '-created_at', '-start_date', '-end_date']},
        ),
        migrations.AlterField(
            model_name='announcement',
            name='is_global',
            field=models.BooleanField(default=False, help_text='If global is checked announcement filter will not work.', verbose_name='is global'),
        ),
    ]
