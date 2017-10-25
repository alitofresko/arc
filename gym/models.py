from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class Member(models.Model):

    #Member data
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.ImageField(upload_to="members/", blank=True, null=True)

    #Contact
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    #Body
    birthday = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weigth = models.IntegerField(blank=True, null=True)

    #Trainer notes
    trainer = models.ForeignKey(User, limit_choices_to={'is_staff': True, 'is_superuser': False}, blank=True, null=True)
    note = models.CharField(max_length=160, blank=True, null=True)

    #Registration status
    registration = models.DateField(auto_now_add=True)
    expiration = models.DateField(blank=True, null=True)


    #card = models.OneToOneField('Card')

    def get_absolute_url(self):
        """
        Returns the url to access a particular member.
        """
        return reverse('member-detail', args=[str(self.id)])

    def __str__(self):
        return u'%s %s' % (self.surname, self.name)

