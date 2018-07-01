from import_export import resources
from .models import Flashcard

class FlashcardResource(resources.ModelResource):
    class Meta:
        model = Flashcard
