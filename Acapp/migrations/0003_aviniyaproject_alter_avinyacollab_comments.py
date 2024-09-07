# Generated by Django 5.1 on 2024-09-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acapp', '0002_avinyacollab'),
    ]

    operations = [
        migrations.CreateModel(
            name='AviniyaProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('loading_image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Started', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='avinyacollab',
            name='Comments',
            field=models.CharField(max_length=50),
        ),
    ]
