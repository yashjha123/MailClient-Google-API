# Generated by Django 2.2.3 on 2019-07-05 17:59

from django.db import migrations
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    dependencies = [
        ('gauth', '0007_sessid_access_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessid',
            name='credential',
            field=oauth2client.contrib.django_util.models.CredentialsField(null=True),
        ),
    ]
