# Generated by Django 2.1.2 on 2019-02-07 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PC', '0004_auto_20190204_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nuevanot',
            name='imagen',
        ),
    ]
