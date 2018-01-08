# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-21 09:42
from __future__ import unicode_literals

from django.core.cache import cache
from django.db import migrations


def rename_placeholder(app, schema_editor):
    EventSettingsStore = app.get_model('pretixbase', 'Event_SettingsStore')

    for setting in EventSettingsStore.objects.all():
        if setting.key == 'mail_text_order_placed':
            new_value = setting.value.replace('{paymentinfo}', '{payment_info}')
            setting.value = new_value
            cache.delete('hierarkey_{}_{}'.format('event', setting.object_id))
            setting.save()


class Migration(migrations.Migration):
    dependencies = [
        ('pretixbase', '0060_auto_20170510_1027'),
    ]

    operations = [
        migrations.RunPython(rename_placeholder, migrations.RunPython.noop)
    ]
