# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comments.comments_date'
        db.add_column('comments', 'comments_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2017, 7, 4, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comments.comments_date'
        db.delete_column('comments', 'comments_date')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article', 'db_table': "'article'"},
            'article_date': ('django.db.models.fields.DateTimeField', [], {}),
            'article_likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'article_text': ('django.db.models.fields.TextField', [], {}),
            'article_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'article.comments': {
            'Meta': {'object_name': 'Comments', 'db_table': "'comments'"},
            'comments_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'comments_date': ('django.db.models.fields.DateTimeField', [], {}),
            'comments_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['article']