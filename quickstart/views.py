from rest_framework import viewsets
from .models import User, Administration, Member, Exercise, Category
from .serializers import UserSerializer, AdministrationSerializer, MemberSerializer, ExerciseSerializer, CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class AdministrationViewSet(viewsets.ModelViewSet):
    model = Administration
    queryset = Administration.objects.all()
    serializer_class = AdministrationSerializer

    def get_queryset(self):
        return Administration.objects.all()

class MemberViewSet(viewsets.ModelViewSet):
    model = Member
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.all()

class ExerciseViewSet(viewsets.ModelViewSet):
    model = Exercise
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return Exercise.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
