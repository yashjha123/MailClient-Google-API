# Generated by Django 2.2.3 on 2019-07-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_wids_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=80, null=True)),
                ('div', models.CharField(max_length=80, null=True)),
                ('label', models.CharField(max_length=80, null=True)),
            ],
        ),
    ]
