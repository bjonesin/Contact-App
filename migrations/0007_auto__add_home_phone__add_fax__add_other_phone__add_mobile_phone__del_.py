# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Home_phone'
        db.create_table(u'contacts_home_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_phone', to=orm['contacts.Contact'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Home_phone'])

        # Adding model 'Fax'
        db.create_table(u'contacts_fax', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fax', to=orm['contacts.Contact'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Fax'])

        # Adding model 'Other_phone'
        db.create_table(u'contacts_other_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='other_phone', to=orm['contacts.Contact'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Other_phone'])

        # Adding model 'Mobile_phone'
        db.create_table(u'contacts_mobile_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mobile_phone', to=orm['contacts.Contact'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Mobile_phone'])

        # Deleting field 'Contact.fax'
        db.delete_column(u'contacts_contact', 'fax')

        # Deleting field 'Contact.mobile_phone'
        db.delete_column(u'contacts_contact', 'mobile_phone')

        # Deleting field 'Contact.other_phone'
        db.delete_column(u'contacts_contact', 'other_phone')

        # Deleting field 'Contact.home_phone'
        db.delete_column(u'contacts_contact', 'home_phone')


    def backwards(self, orm):
        # Deleting model 'Home_phone'
        db.delete_table(u'contacts_home_phone')

        # Deleting model 'Fax'
        db.delete_table(u'contacts_fax')

        # Deleting model 'Other_phone'
        db.delete_table(u'contacts_other_phone')

        # Deleting model 'Mobile_phone'
        db.delete_table(u'contacts_mobile_phone')

        # Adding field 'Contact.fax'
        db.add_column(u'contacts_contact', 'fax',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.mobile_phone'
        db.add_column(u'contacts_contact', 'mobile_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.other_phone'
        db.add_column(u'contacts_contact', 'other_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.home_phone'
        db.add_column(u'contacts_contact', 'home_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


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
        u'contacts.fax': {
            'Meta': {'object_name': 'Fax'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fax'", 'to': u"orm['contacts.Contact']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.home_phone': {
            'Meta': {'object_name': 'Home_phone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_phone'", 'to': u"orm['contacts.Contact']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.mobile_phone': {
            'Meta': {'object_name': 'Mobile_phone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mobile_phone'", 'to': u"orm['contacts.Contact']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.note': {
            'Meta': {'object_name': 'Note'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notes'", 'to': u"orm['contacts.Contact']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.other_phone': {
            'Meta': {'object_name': 'Other_phone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'other_phone'", 'to': u"orm['contacts.Contact']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']