from rest_framework import serializers

from .models import Departement, Employer


class DepartementSerializer(serializers.ModelSerializer):
    """
        Currently unused in preference of the below.
        """
    nom = serializers.CharField(required=True)

    class Meta:
        model = Departement
        fields = ('id', 'nom', 'date_creation')


class EmployerSerializer(serializers.ModelSerializer):
    """
        Currently unused in preference of the below.
        """
    nom = serializers.CharField(required=True)
    prenom = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    tel = serializers.CharField(required=True)
    date_embauche = serializers.DateTimeField(required=False)

    class Meta:
        model = Employer
        fields = ('id', 'departement', 'nom', 'prenom', 'email', 'tel', 'date_embauche', 'createdAt')
