# Generated by Django 5.1 on 2024-09-07 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Acapp', '0003_aviniyaproject_alter_avinyacollab_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aviniyaproject',
            name='loading_image',
        ),
    ]
