# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0003_logentry_detailed_object_repr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='detailed_object_repr',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
