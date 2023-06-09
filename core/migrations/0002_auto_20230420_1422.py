# Generated by Django 2.2.13 on 2023-04-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport Wear'), ('OW', 'OutWear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='clabel',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'success'), ('D', 'dark')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]
