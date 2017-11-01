import csv
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
    
    cat = models.CharField(max_length=3, blank=True, null=True)
    cat_text = models.CharField(max_length=50, blank=True, null=True)
    cert = models.DateField(blank=True, null=True)
    def update_data():
        for m in Member.objects.all():
            Registration.objects.get_or_create(member=m, category=Category.objects.get(category_name='GIOVANI'), payment=Payment.objects.get(payment_name='Daily'))
    def import_data():
        with open('member.csv') as f:
               reader = csv.reader(f, delimiter=';')
               for row in reader:
                  if row[0] != 'surname': #where Person_name is first column's name
                     _, created = Member.objects.get_or_create(
                         surname=row[0],
                         name=row[1],
                         )
    def get_absolute_url(self):
        """
        Returns the url to access a particular member.
        """
        return reverse('member-detail', args=[str(self.id)])

    def __str__(self):
        return u'%s %s' % (self.surname, self.name)
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return u'%s' % (self.category_name)
class Payment(models.Model):
    payment_name = models.CharField(max_length=50)
    valid_days = models.IntegerField(default=0)
    valid_months = models.IntegerField(default=0)
    valid_years = models.IntegerField(default=0)
    
    def __str__(self):
        return u'%s' % (self.payment_name)
    
    
class Registration(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    valid_from = models.DateField(auto_now_add=True)
    valid_until = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return u'%s %s [%s] (%s - %s)' % (self.member.name, self.member.surname, self.category.category_name, self.valid_from, self.valid_until)
