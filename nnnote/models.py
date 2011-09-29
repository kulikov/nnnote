from django.db import models

class NoteItem(models.Model):
    text = models.TextField()
    createDate = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text