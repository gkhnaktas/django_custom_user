# Generated by Django 2.1.2 on 2018-10-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181009_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(db_index=True, default='LjSrNs4bo', max_length=9, verbose_name='uid'),
        ),
    ]
