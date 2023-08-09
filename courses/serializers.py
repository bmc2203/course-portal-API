from rest_framework import serializers
from .models import *

class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = (
            'first_name', 'last_name', 'email', 'created_at', 'updated_at'
        )

class EducatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educator
        fields = (
            'first_name', 'last_name', 'email', 'created_at', 'updated_at'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'educator', 'description', 'content', 'created_at', 'updated_at'
        )

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('course', 'learner', 'grades', 'created_at', 'updated_at'
        )