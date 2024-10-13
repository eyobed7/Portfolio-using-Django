from django.db import models

class About(models.Model):
    short_description=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to="about", default="about/eyobed.jpg")


    class Meta:
        verbose_name="About me"
        verbose_name_plural="About me"

    def __str__(self):
        return "About me"



#service model
class Service(models.Model):
    name=models.CharField(verbose_name="Service name",max_length=100)
    description=models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name

# recent work model
class Recentwork(models.Model):
    title=models.CharField(max_length=100, verbose_name="Work title")
    image=models.ImageField(verbose_name="works")

    def __str__(self):
        return self.title

#client model
class Client(models.Model):
    name=models.CharField(verbose_name="Client name",max_length=100)
    description=models.TextField(verbose_name="Client say")
    image=models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name