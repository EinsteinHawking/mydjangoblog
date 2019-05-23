from django.db import models

# Create your models here.

import mongoengine

class Tags(mongoengine.Document):
    tag_name=mongoengine.StringField()
    tag_url=mongoengine.StringField()
    count = mongoengine.IntField()
    meta = {'collection': 'tags'}

class Work(mongoengine.Document):
    name = mongoengine.StringField()
    author = mongoengine.StringField()
    dynasty = mongoengine.StringField()
    content = mongoengine.StringField()
    tags = mongoengine.ListField()

    wk_objs = models.Manager()
    meta = {'collection':'works'}