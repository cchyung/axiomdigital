from django.db import models
from cms.models.pluginmodel import CMSPlugin


#Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=100, default='title')
    link = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    picture = models.ImageField(upload_to='work/',
                                help_text="This picture needs to have square dimensions or it will render incorrectly.")

    def __str__(self):
        return self.title

class WorkPluginModel(CMSPlugin):
    work = models.ForeignKey(Work)

    def __str__(self):
        return self.work.title
