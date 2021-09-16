from django.contrib import admin

# Register your models here.

from .models import Employer, Departement


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_creation')
    list_filter = ('date_creation',)


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('departement', 'prenom', 'nom', 'email', 'tel', 'date_embauche', 'createdAt')

    def get_sujet(obj):
        return obj.sujet.nom
        get_sujet.short_description = 'employer'


# admin.site.register(models.Departement)
# admin.site.register(models.Employer)
