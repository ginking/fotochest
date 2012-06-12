# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Settings.enable_download'
        db.add_column('administrator_settings', 'enable_download', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Settings.enable_download'
        db.delete_column('administrator_settings', 'enable_download')


    models = {
        'administrator.settings': {
            'Meta': {'object_name': 'Settings'},
            'app_name': ('django.db.models.fields.CharField', [], {'default': "'FotoChest'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'enable_download': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['administrator']
