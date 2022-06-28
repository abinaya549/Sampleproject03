from rest_framework import serializers
from .models import Student, StudentMark


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    marks = MarksSerializer(read_only=True, many=True)

    class Meta:
        model = Student
        fields = "__all__"
