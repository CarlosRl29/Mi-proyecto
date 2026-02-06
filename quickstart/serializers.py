from rest_framework import serializers
from .models import User, Administration, Member, Exercise, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        model = self.meta.model
        return model.objects.create_user(**validated_data)
        
class AdministrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administration
        fields =(
            'user'
        )

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields =(
            'user',
            'address',
            'birthdate'
        )

    def create(self, valideted_data):
        user = User.objects.create(
            **valideted_data.pop("user")
        )
        valideted_data["user"] = user
        instance = super().create(valideted_data)
        return instance 
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Exercise
        fields = "__all__"

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category, created = Category.objects.get_or_create(**category_data)
        exercise = Exercise.objects.create(category=category, **validated_data)
        return exercise 
