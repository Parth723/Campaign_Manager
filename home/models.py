from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    