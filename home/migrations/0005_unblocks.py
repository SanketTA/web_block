# Generated by Django 4.0.1 on 2022-09-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_blocks_unblocked_blocks_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unblocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unblocked', models.CharField(max_length=122)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
