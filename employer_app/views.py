from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Departement, Employer
from .serializers import DepartementSerializer, EmployerSerializer


# Create your views here.

#  ############################ Departement Views ##############################
class DepartementList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DepartementSerializer(queryset, many=True)
        return Response(serializer.data)


class DepartementCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]

    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DepartementSerializer(queryset, many=True)
        return Response(serializer.data)


class DepartementDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

    def get_queryset(self):
        nom = self.kwargs['pk']
        print(nom)
        return Departement.objects.filter(id=nom)


class EditDepartement(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


class DeleteDepartement(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()


class DepartementListDetailFilter(generics.ListAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^nom']


# class DepartementSearch(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Departement.objects.all()
#     serializer_class = DepartementSerializer
#     filter_backends = [filters.SearchFilter]


#  ############################ Employer Views ##############################
class EmployerList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EmployerSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployerCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EmployerSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployerDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def get_queryset(self):
        prenom = self.kwargs['pk']
        print(prenom)
        return Employer.objects.filter(id=prenom)


class EditEmployer(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class DeleteEmployer(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployerListDetailFilter(generics.ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^prenom']


# class EmployerSearch(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Employer.objects.all()
#     serializer_class = EmployerSerializer
#     filter_backends = [filters.SearchFilter]
