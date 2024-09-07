from django.db import models

# Create your models here.

class Avinyacontact(models.Model):
    Name = models.CharField(max_length=50)
    Number = models.CharField(max_length=20)
    Email= models.EmailField(max_length=50)
    Message= models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name
    
class Avinyacollab(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=20)
    CompanyName = models.CharField(max_length=50)
    Industry = models.CharField(max_length=50)
    Comments =  models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"
    
    
# models.py
from django.db import models

class AviniyaProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    main_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=50,
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')],
        default='Not Started'
    )
    def __str__(self):
        return self.name
