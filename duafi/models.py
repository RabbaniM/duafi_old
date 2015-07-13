from django.db import models




#Start========================================================================
# For Contact

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    massage = models.CharField(max_length=300)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.email
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.subject
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.massage

#End========================================================================

