# Generated by Django 2.1.2 on 2019-02-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC', '0007_auto_20190219_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuevanot',
            name='imagen',
            field=models.ImageField(default='', upload_to='img'),
        ),
    ]
