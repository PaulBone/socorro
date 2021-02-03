# Generated by Django 1.11.16 on 2018-12-14 19:51

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("status", "0002_auto_20180522_1545")]

    operations = [
        migrations.AlterField(
            model_name="statusmessage",
            name="severity",
            field=models.CharField(
                choices=[
                    ("info", "Info"),
                    ("warning", "Warning"),
                    ("critical", "Critical"),
                ],
                max_length=20,
            ),
        )
    ]
