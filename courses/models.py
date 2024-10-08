from django.db import models

# Create your models here.
class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMMING_SOON = "soon", "Comming Soon"
    DRAFT = "draft", "Draft"

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email Required"
    DRAFT = "draft", "Draft"



class Course(models.Model):
    title = models.CharField(max_length = 150)
    descraption = models.TextField(max_length=255, null=True, blank=True)
    image = " " 
    status = models.CharField(max_length=16,choices=PublishStatus.choices,
                            default= PublishStatus.DRAFT )
    access = models.CharField(max_length=16,choices=AccessRequirement.choices,
                            default= AccessRequirement.DRAFT )
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUblished