from django.urls import path
from .views import *

app_name = 'employer_app'

urlpatterns = [
    # Departement URLS
    path('departement/', DepartementList.as_view(), name='departement_listes'),
    path('creer/departement/', DepartementCreate.as_view(), name='creer_departement'),
    path('departement-detail/<int:pk>/', DepartementDetail.as_view(), name='departement_details'),
    path('departement/edit/<int:pk>/', EditDepartement.as_view(), name='edit_departement'),
    path('departement/delete/<int:pk>/', DeleteDepartement.as_view(), name='delete_departement'),
    # path('departementSearch/', DepartementSearch.as_view(), name='rechercher_departement'),
    path('departementSearch/custom/', DepartementListDetailFilter.as_view(), name='rechercher_departement'),

    # Employer URLS
    path('employer/', EmployerList.as_view(), name='employer_listes'),
    path('creer/employer/', EmployerCreate.as_view(), name='creer_employer'),
    path('employer-detail/<int:pk>/', EmployerDetail.as_view(), name='employer_details'),
    path('employer/edit/<int:pk>/', EditEmployer.as_view(), name='edit_employer'),
    path('employer/delete/<int:pk>/', DeleteEmployer.as_view(), name='delete_employer'),
    # path('employerSearch/', EmployerSearch.as_view(), name='rechercher_employer'),
    path('employerSearch/custom/', EmployerListDetailFilter.as_view(), name='rechercher_employer'),
]
