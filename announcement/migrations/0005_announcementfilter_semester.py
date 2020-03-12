# Generated by Django 3.0.3 on 2020-03-12 05:37

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0004_auto_20200312_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementfilter',
            name='semester',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Semester 1'), (2, 'Semester 2'), (3, 'Semester 3'), (4, 'Semester 4'), (5, 'Semester 5'), (6, 'Semester 6'), (7, 'Semester 7'), (8, 'Semester 8')], default=1, max_length=15),
        ),
    ]