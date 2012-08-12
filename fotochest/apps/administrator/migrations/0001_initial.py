# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('administrator_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(default='FotoChest', max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('administrator', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('administrator_settings')


    models = {
        'administrator.settings': {
            'Meta': {'object_name': 'Settings'},
            'app_name': ('django.db.models.fields.CharField', [], {'default': "'FotoChest'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['administrator']
