from django.contrib.auth.models import User
from django.db import models

class Group_Data(models.Model):
        group=models.CharField(max_length=10)


class Student_Data(models.Model):
        Group_Data= models.ForeignKey(Group_Data, on_delete=models.CASCADE, default=None)
        #User=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
        name=models.CharField(max_length=19,null=True)
        mobile=models.CharField(max_length=16,null=True)
        email=models.EmailField(null=True)
        #password = models.CharField(max_length=20, null=True)
        #confirmpassword=models.CharField(max_length=20,null=True)
        address=models.TextField(null=True)
        #gender=models.BooleanField(null=False)
       # marks=models.FloatField()
        gender = models.CharField(max_length=7,null=True)
        countries=models.CharField(max_length=20,null=True)
        #branches=models.CharField(max_length=20,null=True)



        def __str__(self):
                return self.name+str(self.id)