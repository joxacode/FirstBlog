from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProfileData(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_data")
    description = models.TextField()

    def __str__(self):
        return self.name


class SocialLinks(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    url = models.URLField(max_length=240)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order", )

    def __str__(self):
        return self.name


class Posts(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="posts")
    body = models.TextField()

    def __str__(self):
        return self.title


class About(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="about")
    description = models.TextField()

    def __str__(self):
        return self.title




