# Generated by Django 3.2.9 on 2021-12-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overall_rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]