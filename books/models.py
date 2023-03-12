from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Category"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):
    class Meta:
        verbose_name_plural = "Books"

    name = models.CharField(max_length=100)
    author = models.TextField()
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
