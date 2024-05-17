from rest_framework import serializers
from PrepaDuPrepa.models import user,course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= user
        fields=('userId',
                'username',
                'email',
                'role')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= course
        fields=('courseId',
                'title',
                'description',
                'level',
                'subject')