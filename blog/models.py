from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the model first

        if self.featured_image:
            img = Image.open(self.featured_image)

            # Example: Resize the image
            max_size = (800, 800)  # Adjust dimensions as needed
            img.thumbnail(max_size)

            # Save the processed image back to the ImageField
            output = BytesIO()
            img.save(output, format='JPEG', quality=85)  # Adjust format and quality

            output.seek(0)
            self.featured_image = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.featured_image.name.split('.')[0]}.jpg",  # Use .jpg or other format
                'image/jpeg',
                sys.getsizeof(output),
                None
            )

            super().save(*args, **kwargs) # Save the modified imagefield.