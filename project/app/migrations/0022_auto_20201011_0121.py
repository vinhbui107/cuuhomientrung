# Generated by Django 3.1.2 on 2020-10-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20201011_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtubeclip',
            old_name='checked_date',
            new_name='last_live_checked_date',
        ),
        migrations.AlterField(
            model_name='youtubeclip',
            name='live_status',
            field=models.IntegerField(choices=[(0, 'Chưa kiểm tra'), (1, 'Đang kiểm tra'), (2, 'Die-YT'), (3, 'Gov-YT'), (4, 'Live-YT'), (5, 'Bad Link')], default=5, verbose_name='Trạng thái'),
        ),
    ]
