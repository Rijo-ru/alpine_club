from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=255)
    height = models.IntegerField()
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Climber(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Climb(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    climbers = models.ManyToManyField(Climber)

    def __str__(self):
        return f"Climb of {self.mountain.name} from {self.start_date} to {self.end_date}"
