# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('article_text', self.gf('django.db.models.fields.TextField')()),
            ('article_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('article_likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'article', ['Article'])

        # Adding model 'Comments'
        db.create_table('comments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments_text', self.gf('django.db.models.fields.TextField')()),
            ('comments_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['article.Article'])),
        ))
        db.send_create_signal(u'article', ['Comments'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('article')

        # Deleting model 'Comments'
        db.delete_table('comments')


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
            'comments_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['article']