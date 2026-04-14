import json
from django.core.management.base import BaseCommand
from dictionary.models import Language, Word


class Command(BaseCommand):
    help = 'Import Hyolmo words from JSON file'

    def handle(self, *args, **kwargs):
        language, created = Language.objects.get_or_create(
            code='hyo',
            defaults={
                'name': 'Hyolmo',
                'description': 'Tibetan dialect spoken in Helambu region of Nepal',
                'is_active': True
            }
        )

        with open('hyolmo_words.json', encoding='utf-8') as f:
            words = json.load(f)

        count = 0
        for w in words:
            if w['original_word']:
                Word.objects.get_or_create(
                    original_word=w['original_word'],
                    language=language,
                    defaults={
                        'english_meaning': w.get('english_meaning', ''),
                        'pronunciation': w.get('pronunciation', ''),
                        'part_of_speech': w.get('part_of_speech', ''),
                    }
                )
                count += 1

        self.stdout.write(f"Successfully imported {count} words")