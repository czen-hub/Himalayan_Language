from django.contrib import admin
from .models import Language, Word, Phrase, Category, CrossReference


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'is_active']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['original_word', 'language', 'part_of_speech']
    list_filter = ['language', 'part_of_speech']
    search_fields = ['original_word', 'english_meaning']


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['original_phrase', 'language', 'context']
    list_filter = ['language', 'context']
    search_fields = ['original_phrase', 'english_meaning']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CrossReference)
class CrossReferenceAdmin(admin.ModelAdmin):
    list_display = ['source_word', 'target_word', 'relationship']