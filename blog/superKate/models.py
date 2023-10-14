from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.is_private}"

class Post(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()

    page = models.OneToOneField(Page, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Review(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.name} - {self.content}"


class Posts(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()

    review = models.ManyToManyField(Review)

    def __str__(self):
        return f"{self.pk} - {self.name}"