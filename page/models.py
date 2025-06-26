from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    STAR_CHOICES = (
        (1 , "1 star"),
        (2 , "2 star"),
        (3 , "3 star"),
        (4 , "4 star"),
        (5 , "5 star"),
    )
    star = models.IntegerField(choices = STAR_CHOICES )
    description = RichTextUploadingField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    slug = models.SlugField(unique = True ,blank = True ,max_length= 255)
    image_main = models.ImageField(upload_to="blog/image/")

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate if slug is not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
