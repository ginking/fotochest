# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Album.slug'
        db.add_column('photo_manager_album', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, db_index=True), keep_default=False)

        # Adding field 'Album.description'
        db.add_column('photo_manager_album', 'description', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Photo.file_name'
        db.add_column('photo_manager_photo', 'file_name', self.gf('django.db.models.fields.CharField')(default='', max_length=400), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Album.slug'
        db.delete_column('photo_manager_album', 'slug')

        # Deleting field 'Album.description'
        db.delete_column('photo_manager_album', 'description')

        # Deleting field 'Photo.file_name'
        db.delete_column('photo_manager_photo', 'file_name')


    models = {
        'photo_manager.album': {
            'Meta': {'object_name': 'Album'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photo_manager.Album']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'photo_manager.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photo_manager.Album']"}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['photo_manager']
