from django.db import models
from django.contrib import admin

class Flow(models.Model):
    beginTime   = models.DateTimeField()
    size        = models.IntegerField()
    behavior    = models.ForeignKey('Behavior', db_index = True)
    os          = models.CharField(max_length = 100, db_index = True)
    srcIp       = models.GenericIPAddressField(db_index = True)
    srcPort     = models.IntegerField()
    dstIp       = models.GenericIPAddressField(db_index = True)
    dstPort     = models.IntegerField()
    protocol    = models.ForeignKey('Protocol', db_index = True)

    def __unicode__(self):
        return "Flow %s" % (self.id)

class App(models.Model):
    name    = models.CharField(max_length = 100, db_index = True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Behavior(models.Model):
    name    = models.CharField(max_length = 100, db_index = True)
    app     = models.ForeignKey('App')

    class Meta:
        ordering = ['app', 'name']

    def __unicode__(self):
        return "%s >> %s" % (self.app.name, self.name)

class Protocol(models.Model):
    name    = models.CharField(max_length = 100, db_index = True)

    def __unicode__(self):
        return self.name

class OS(models.Model):
    name    = models.CharField(max_length = 100, db_index = True)

    def __unicode__(self):
        return self.name

admin.site.register(Flow)
admin.site.register(App)
admin.site.register(Behavior)
admin.site.register(Protocol)
admin.site.register(OS)
