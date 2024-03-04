# Ex02 Django ORM Web Application
## Date: 28/02/24

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![Screenshot 2024-02-28 163704](https://github.com/Lathika2006/ORM/assets/148959215/02cdf033-5e28-4dbd-8f6b-e8f09e9c5e15)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

from django.db import models
from django.contrib import admin
class Book_Details(models.Model):
	Book_name=models.CharField(max_length=100)
	Book_serial_number=models.IntegerField(primary_key="Book_serial_number")
	author_name=models.CharField(max_length=30)
	No_of_pages=models.IntegerField()
	Genre=models.CharField(max_length=100)
	No_of_Characters=models.IntegerField()
	No_of_Chapters=models.IntegerField()
	Year=models.IntegerField(max_length=4,help_text="Published")
class Book_DetailsAdmin(admin.ModelAdmin):
	list_Display=("Book_name","Book_serial_number","author_name","No_of_pages","Genre","No_of_Characters","No_of_Chapters","Year");

admin.py

from django .contrib import admin
from .models import Book_Details,Book_DetailsAdmin
admin.site.register(Book_Details,Book_DetailsAdmin)cg
```
## OUTPUT
![Uploading Screenshot 2024-02-28 093754.png…]()


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
