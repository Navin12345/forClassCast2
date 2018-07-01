from django.contrib import admin
from . models import Flashcard
from import_export.admin import ImportExportModelAdmin

@admin.register(Flashcard)
class FlashcardAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
