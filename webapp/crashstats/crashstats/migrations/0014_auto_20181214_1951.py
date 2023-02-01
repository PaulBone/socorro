# Generated by Django 1.11.16 on 2018-12-14 19:51

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("crashstats", "0013_1507916_major_version_data_migration")]

    operations = [
        migrations.AlterField(
            model_name="bugassociation",
            name="bug_id",
            field=models.IntegerField(help_text="Bugzilla bug id"),
        ),
        migrations.AlterField(
            model_name="bugassociation",
            name="signature",
            field=models.TextField(help_text="Socorro-style crash report signature"),
        ),
        migrations.AlterField(
            model_name="platform",
            name="name",
            field=models.CharField(
                help_text="Name of the platform", max_length=20, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="platform",
            name="short_name",
            field=models.CharField(
                help_text="Short abbreviated name of the platform", max_length=20
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="whether or not this product is active and should show up on the site",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(
                help_text="ProductName of product as it appears in crash reports",
                max_length=50,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="sort",
            field=models.IntegerField(
                default=100, help_text="sort order spot for this product"
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="archive_url",
            field=models.TextField(
                blank=True,
                help_text="the url on archive.mozilla.org for data on this build",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="build_id",
            field=models.CharField(
                help_text="the build id for this version", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="major_version",
            field=models.IntegerField(
                help_text='major version of this version; for example "63.0b4" would be 63'
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="product_name",
            field=models.CharField(
                help_text="ProductName of product as it appears in crash reports",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="release_channel",
            field=models.CharField(
                help_text="release channel for this version", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="release_version",
            field=models.CharField(
                help_text="version as it appears in crash reports", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="productversion",
            name="version_string",
            field=models.CharField(help_text="actual version", max_length=50),
        ),
        migrations.AlterField(
            model_name="signature",
            name="first_build",
            field=models.BigIntegerField(
                help_text="the first build id this signature was seen in"
            ),
        ),
        migrations.AlterField(
            model_name="signature",
            name="first_date",
            field=models.DateTimeField(
                help_text="the first crash report date this signature was seen in"
            ),
        ),
        migrations.AlterField(
            model_name="signature",
            name="signature",
            field=models.TextField(help_text="the crash report signature", unique=True),
        ),
    ]
