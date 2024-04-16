from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
    ('M', 'Morning Reading'), 
    ('B', 'Bedtime Reading')
) 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    introduction = models.TextField(max_length=500)
    publish_year = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
    def read_for_today(self):
        return self.reading_set.filter(date=date.today()).count() >= len(TIMES)

  
class Reading(models.Model):
    date = models.DateField('Reading date')
    time = models.CharField(
        max_length=1,
        choices=TIMES, 
        default=TIMES[0][0]
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

