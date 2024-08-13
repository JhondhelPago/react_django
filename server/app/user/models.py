from django.db import models

# Create your models here.


class user(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, null=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    class Meta:

        db_table = 'user' 

    # return an fstring about the properties of the user model
    def displayProperties(self):

        return f"id: ${self.id}, username: ${self.username}, age: ${self.age}, gender: ${self.gender}, email: ${self.email}, password: ${self.password}"
    


class order(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.IntegerField(default=0)


    class Meta:

        db_table = 'order'


    #return an fstring about the properties of the order model
    def details(self):

        return f"id: ${self.id}, user_id: ${self.user_id}, product_id: ${self.product_id}"
    
