from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name='نام')
    parent_id = models.ForeignKey("self", on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title