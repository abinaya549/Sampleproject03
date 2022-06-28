# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Student, StudentMark
from .serializers import StudentSerializer, MarksSerializer


class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentMark(ModelViewSet):
    serializer_class = MarksSerializer
    queryset = StudentMark.objects.all()

