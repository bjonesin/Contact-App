# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Home_phone'
        db.delete_table(u'contacts_home_phone')

        # Deleting model 'Fax'
        db.delete_table(u'contacts_fax')

        # Deleting model 'Other_phone'
        db.delete_table(u'contacts_other_phone')

        # Deleting model 'Mobile_phone'
        db.delete_table(u'contacts_mobile_phone')

        # Adding model 'Phone'
        db.create_table(u'contacts_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phone', to=orm['contacts.Contact'])),
            ('choice', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'contacts', ['Phone'])


    def backwards(self, orm):
        # Adding model 'Home_phone'
        db.create_table(u'contacts_home_phone', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_phone', to=orm['contacts.Contact'])),
        ))
        db.send_create_signal(u'contacts', ['Home_phone'])

        # Adding model 'Fax'
        db.create_table(u'contacts_fax', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fax', to=orm['contacts.Contact'])),
        ))
        db.send_create_signal(u'contacts', ['Fax'])

        # Adding model 'Other_phone'
        db.create_table(u'contacts_other_phone', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='other_phone', to=orm['contacts.Contact'])),
        ))
        db.send_create_signal(u'contacts', ['Other_phone'])

        # Adding model 'Mobile_phone'
        db.create_table(u'contacts_mobile_phone', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mobile_phone', to=orm['contacts.Contact'])),
        ))
        db.send_create_signal(u'contacts', ['Mobile_phone'])

        # Deleting model 'Phone'
        db.delete_table(u'contacts_phone')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'contacts.note': {
            'Meta': {'object_name': 'Note'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notes'", 'to': u"orm['contacts.Contact']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.phone': {
            'Meta': {'object_name': 'Phone'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']