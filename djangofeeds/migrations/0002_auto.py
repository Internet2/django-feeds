# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field categories on 'Feed'
        db.delete_table('djangofeeds_feed_categories')


    def backwards(self, orm):
        # Adding M2M table for field categories on 'Feed'
        db.create_table('djangofeeds_feed_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feed', models.ForeignKey(orm['djangofeeds.feed'], null=False)),
            ('category', models.ForeignKey(orm['djangofeeds.category'], null=False))
        ))
        db.create_unique('djangofeeds_feed_categories', ['feed_id', 'category_id'])


    models = {
        'djangofeeds.category': {
            'Meta': {'unique_together': "(('name', 'domain'),)", 'object_name': 'Category'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'djangofeeds.enclosure': {
            'Meta': {'object_name': 'Enclosure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'djangofeeds.feed': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Feed'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_last_refresh': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_last_requested': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'feed_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'freq': ('django.db.models.fields.IntegerField', [], {'default': '10800'}),
            'http_etag': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'http_last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_error': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ratio': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'sort': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'djangofeeds.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['djangofeeds.Category']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'enclosures': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['djangofeeds.Enclosure']", 'symmetrical': 'False', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djangofeeds.Feed']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '2048'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['djangofeeds']