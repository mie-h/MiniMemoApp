from django.db import models


class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

# class Category(models.Model):
#     category = models.CharField(max_length=40, null=True)

#     def __str__(self):
#         return self.category


# class TodoList(models.Model):
#     text = models.CharField(max_length=100)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.text