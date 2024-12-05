from django.db import models 
 
class Author(models.Model): 
    name = models.CharField(max_length=100) 
    biography = models.TextField(blank=True) 
 
    def __str__(self): 
        return self.name 
 
class Book(models.Model): 
    title = models.CharField(max_length=150) 
    description = models.TextField(blank=True) 
    published_date = models.DateField() 
    author = models.ForeignKey(Author, related_name='books', 
on_delete=models.CASCADE) 
 
    def __str__(self): 
        return self.title 