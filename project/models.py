from django.db import models

class Tutorial(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.name
    
    
class Video(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=256)
    video = models.FileField(upload_to='videos/')
    
    
    def __str__(self) -> str:
        return self.title
    