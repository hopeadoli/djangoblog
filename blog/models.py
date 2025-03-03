# from django.conf import settings
# from django.db import models
# from django.utils import timezone
# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile
# import sys


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#     featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)  # Save the model first

#         if self.featured_image:
#             img = Image.open(self.featured_image)

#             # Example: Resize the image
#             max_size = (800, 800)  # Adjust dimensions as needed
#             img.thumbnail(max_size)

#             # Save the processed image back to the ImageField
#             output = BytesIO()
#             img.save(output, format='JPEG', quality=85)  # Adjust format and quality

#             output.seek(0)
#             self.featured_image = InMemoryUploadedFile(
#                 output,
#                 'ImageField',
#                 f"{self.featured_image.name.split('.')[0]}.jpg",  # Use .jpg or other format
#                 'image/jpeg',
#                 sys.getsizeof(output),
#                 None
#             )

#             super().save(*args, **kwargs) # Save the modified imagefield.



from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.http import HttpResponseBadRequest
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


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
    
    def save_multiple_formats(image_file, output_base_name):
        img = Image.open(image_file)

        # Save as JPEG
        output_jpeg = BytesIO()
        img.save(output_jpeg, format='JPEG', quality=85)
        with open(f"{output_base_name}.jpg", "wb") as f:
            f.write(output_jpeg.getvalue())

        # Save as PNG
        output_png = BytesIO()
        img.save(output_png, format='PNG')
        with open(f"{output_base_name}.png", "wb") as f:
            f.write(output_png.getvalue())
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the model first

        if self.featured_image:
            img = Image.open(self.featured_image)

            # Example: Resize the image
            # max_size = (800, 800)  # Adjust dimensions as needed
            # img.thumbnail(max_size)

            # Save the processed image back to the ImageField
            output = BytesIO()
            # img.save(output, format='JPEG', quality=85)   Adjust format and quality

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



class UploadView(View):
    def post(self, request, *args, **kwargs):
        # Get the uploaded file
        uploaded_file = request.FILES.get('file')
        
        if not uploaded_file:
            return HttpResponseBadRequest('No file uploaded.')

        # Check Content-Type in the header
        allowed_content_types = ['image/jpeg', 'image/png', 'image/gif']
        if uploaded_file.content_type not in allowed_content_types:
            return HttpResponseBadRequest('Unsupported file type.')

        # Save the file if it's valid
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        return JsonResponse({'file_url': file_url})