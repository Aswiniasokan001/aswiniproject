# Generated by Django 4.1.7 on 2023-03-20 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveproject', '0004_remove_condact_tb_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_enter_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
