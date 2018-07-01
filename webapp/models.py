from django.db import models

class Flashcard(models.Model):
    Chapter=models.CharField(max_length=20)
    Subject=models.CharField(max_length=20)
    Class=models.CharField(max_length=20)
    Link=models.CharField(max_length=1000)
    Total_for_that_chapter=models.IntegerField()
    Serial_Number=models.IntegerField()
    #Serial_number=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    def __str__(self):
        return self.Subject + ' - ' + self.Class  + ' - ' + self.Chapter
