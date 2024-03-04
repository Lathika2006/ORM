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
	list_display=("Book_name","Book_serial_number","author_name","No_of_pages","Genre","No_of_Characters","No_of_Chapters","Year");

