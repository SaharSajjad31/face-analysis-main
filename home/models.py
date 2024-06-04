from django.contrib.auth.models import User
from django.db import models


class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Specify the upload directory
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)



