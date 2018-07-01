from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flashcard
from .serializers import FlashcardSerializer
from tablib import Dataset

class FlashcardList(APIView):
    

    def get(self, request, Chapter,Class,Subject):
        Flashcard1 =Flashcard.objects.filter(Chapter = Chapter, Class=Class, Subject=Subject)
        serializer=FlashcardSerializer(Flashcard1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def simple_upload(request):
    if request.method == 'POST':
        Flashcard_resource = FlashcardResource()
        dataset = Dataset()
        new_Flashcard = request.FILES['myfile']

        imported_data = dataset.load(new_Flashcard.read())
        result = Flashcard_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            Flasgcard_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
