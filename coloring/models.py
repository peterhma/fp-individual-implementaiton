
# Create the Drawing model
from django.db import models

# The Author model has been created for you
class Author(models.Model):
  name = models.CharField(max_length=50)

# Create the Drawing model
class Drawing(models.Model):
  title = models.CharField(max_length=50)
  author = models.ForeignKey('Author', on_delete=models.CASCADE,)
  points = models.JSONField()

  




