# Generated by Django 2.2.1 on 2019-06-23 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0043_remove_review_personid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='upvotes',
        ),
    ]
