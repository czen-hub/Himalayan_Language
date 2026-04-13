from django.db import models
# importing Django's model module — everything below inherits from this


class Language(models.Model):
    # models.Model means this class is a database table
    
    name = models.CharField(max_length=100)
    # CharField = text field with a max length limit
    # use for short text — names, titles, codes
    
    code = models.CharField(max_length=10)
    # short code for the language — hyo, shr, tam, tib
    
    description = models.TextField(blank=True)
    # TextField = long text, no max length
    # blank=True means this field is optional — can be left empty
    
    is_active = models.BooleanField(default=True)
    # BooleanField = True or False only
    # default=True means new languages are active unless you say otherwise

    def __str__(self):
        return self.name
    # __str__ controls what shows in Django admin
    # without this admin shows "Language object (1)" — not helpful
    # with this it shows "Hyolmo" — much cleaner


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    # ForeignKey = relationship to another table
    # every Word belongs to one Language
    # on_delete=CASCADE means if you delete a Language,
    # all its Words get deleted too
    
    original_word = models.CharField(max_length=200)
    # the actual word in Hyolmo/Sherpa/etc
    
    english_meaning = models.TextField()
    # no blank=True here — english meaning is required
    
    nepali_meaning = models.TextField(blank=True)
    # optional — not every word will have Nepali translation yet
    
    pronunciation = models.CharField(max_length=200, blank=True)
    # how to say the word — optional
    
    part_of_speech = models.CharField(max_length=50)
    # noun, verb, adjective — required
    
    example_sentence = models.TextField(blank=True)
    # optional example usage
    
    audio_file = models.FileField(upload_to='audio/words/', blank=True)
    # FileField = stores a file (audio recording)
    # upload_to tells Django which folder to save it in
    # blank=True because most words won't have audio at first

    def __str__(self):
        return f"{self.original_word} ({self.language})"
    # f-string — combines the word and its language
    # shows "khamchi (Hyolmo)" in admin


class Phrase(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    # same relationship as Word — belongs to a Language
    
    original_phrase = models.CharField(max_length=500)
    # longer than Word so max_length is 500 not 200
    
    english_meaning = models.TextField()
    nepali_meaning = models.TextField(blank=True)
    pronunciation = models.CharField(max_length=500, blank=True)
    
    context = models.CharField(max_length=50)
    # formal, informal, greeting, farewell, travel
    # required — every phrase needs a context label
    
    audio_file = models.FileField(upload_to='audio/phrases/', blank=True)
    # separate folder from words — keeps audio organized

    def __str__(self):
        return f"{self.original_phrase} ({self.language})"


class Category(models.Model):
    name = models.CharField(max_length=100)
    # greetings, food, family, numbers, travel
    
    words = models.ManyToManyField(Word, blank=True)
    # ManyToManyField = a word can belong to multiple categories
    # and a category can have multiple words
    # example: "eat" can be in both "food" and "daily verbs"
    # blank=True — category can exist with no words yet
    
    phrases = models.ManyToManyField(Phrase, blank=True)
    # same idea for phrases

    def __str__(self):
        return self.name


class CrossReference(models.Model):
    source_word = models.ForeignKey(Word, related_name='source', on_delete=models.CASCADE)
    # the word you're comparing FROM
    # related_name='source' — needed because we have two ForeignKeys
    # to the same model (Word), Django needs unique names to tell them apart
    
    target_word = models.ForeignKey(Word, related_name='target', on_delete=models.CASCADE)
    # the word you're comparing TO
    # example: Hyolmo "me" (fire) → Tibetan "me" (fire)
    
    relationship = models.CharField(max_length=100)
    # "same meaning", "similar", "dialect variant"

    def __str__(self):
        return f"{self.source_word} → {self.target_word}"
        # shows "me (Hyolmo) → me (Tibetan)" in admin