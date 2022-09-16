from modeltranslation.translator import translator, TranslationOptions
from .models import Person


class PersonTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)


translator.register(Person, PersonTranslationOptions)
