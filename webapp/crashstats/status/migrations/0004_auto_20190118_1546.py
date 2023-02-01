# Generated by Django 2.1.5 on 2019-01-18 15:46

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("status", "0003_auto_20181214_1951")]

    operations = [
        migrations.AlterField(
            model_name="statusmessage",
            name="message",
            field=models.TextField(
                help_text='Plain text, but will linkify "bug #XXXXXXX" strings'
            ),
        )
    ]
