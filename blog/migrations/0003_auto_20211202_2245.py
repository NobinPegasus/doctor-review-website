# Generated by Django 3.2.9 on 2021-12-02 16:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='Ka-132/2, Rampura', max_length=100, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='chamber',
            field=models.CharField(default='Apollo', max_length=200, verbose_name="Chamber's Name"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=2, max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='fees',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='hours',
            field=models.TimeField(default='11:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Specialty'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name="Doctor's Name"),
        ),
    ]
