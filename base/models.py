from django.db import models
from django.contrib.auth.models import User



class Areas(models.Model):
    area_id             = models.AutoField(primary_key=True, editable=False)
    area_name           = models.CharField(max_length=50, null=False, default='New Area')
    area_description    = models.CharField(max_length=500, null=True, blank=True, default='No description available')
    
    def __str__(self) -> str:
        return self.area_name 


class Creator(models.Model):
    """
    """
    user                = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creator_username    = models.CharField(max_length=50, null=False)
    creator_id          = models.AutoField(primary_key=True, null = False, editable=False)


    def __str__(self) -> str:
        return self.creator_username


class Project(models.Model):
    project_id          = models.AutoField(primary_key=True, editable=False)
    creator_id          = models.ForeignKey(Creator, on_delete=models.SET_DEFAULT, default=1)
    # models.SET_NULL --> if creator that created the Project get's deleted, the Project will stay
    project_title       = models.CharField(max_length=200, null=True, blank=False)


    def __str__(self) -> str:
        return self.project_title 

    def save(self, *args, **kwargs):
        if self.creator_id:
            self.creator_username = self.creator_id.creator_username
        super().save(*args, **kwargs)

 