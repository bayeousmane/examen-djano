from django.db import models
from django.utils import timezone


# Create your models here.


class Departement(models.Model):
    nom = models.CharField(max_length=255)
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation")

    class Meta:
        verbose_name_plural = "departements"

    def __str__(self):
        return self.nom


class Employer(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, null=False)
    prenom = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    tel = models.CharField(max_length=25, null=False)
    date_embauche = models.DateTimeField(default=timezone.now, verbose_name="Date embauche")
    createdAt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "employers"

    def __str__(self):
        return f"{self.prenom} {self.nom}"
