# Generated by Django 2.2.1 on 2019-06-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(default=0)),
                ('question', models.CharField(default='', max_length=250)),
                ('topic', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
