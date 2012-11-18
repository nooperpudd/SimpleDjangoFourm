# encoding:utf-8

from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
    """docstring for Forum"""
    title = models.CharField(max_length=60)

    def num_posts(self):
        return sum([t.num_posts() for t in self.thread_set.all()])

    def last_post(self):
        if self.thread_set.count():
            last=None
            for t in self.thread_set.all():
                l=t.last_post()
                if l:
                    if not last:
                        last=1
                    elif l.created>last.created:
                        last=1
            return last
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="论坛"
        verbose_name_plural="论坛"


class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    def num_posts(self):
        return self.post_set.count()
    def num_replies(self):
        return self.post_set.count()-1
    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]
    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return u'%s - %s - %s' % (self.creator, self.thread, self.title)

    def short(self):
        return u"%s - %s \n %s" % (self.creator, self.title, self.creator.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True
