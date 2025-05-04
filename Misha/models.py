from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name='category'
    def __str__(self) -> str:
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural='NEWS'
        verbose_name='NEW'
    def __str__(self) -> str:
        return self.title
