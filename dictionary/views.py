from rest_framework import viewsets, filters
from .models import Language, Word, Phrase, Category, CrossReference
from .serializers import LanguageSerializer, WordSerializer, PhraseSerializer, CategorySerializer, CrossReferenceSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['original_word', 'english_meaning', 'nepali_meaning']


class PhraseViewSet(viewsets.ModelViewSet):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['original_phrase', 'english_meaning']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CrossReferenceViewSet(viewsets.ModelViewSet):
    queryset = CrossReference.objects.all()
    serializer_class = CrossReferenceSerializer