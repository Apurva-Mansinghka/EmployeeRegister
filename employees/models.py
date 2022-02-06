from django.db import models

# Create your models here.
class BloodGroup(models.Model):
    bloodGrp = models.CharField(max_length=5)

    def __str__(self):
        return(self.bloodGrp)
     
class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=15)
    emailID = models.EmailField()   
    dateOfBirth = models.DateField()
    address = models.CharField(max_length=200)
    bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)

    def __str__(self):
        return(self.fullName)
    