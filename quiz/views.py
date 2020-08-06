from rest_framework import viewsets
from .models import *
from .serializers import *


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        if self.action == 'list':
            if not self.request.user.is_superuser:
                return Quiz.objects.filter(is_active=True)
        return Quiz.objects.all()
