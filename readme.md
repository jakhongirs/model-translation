# Model Translation

#### This is a simple example of how to translate a model from one language to another.

## Setup

1. ```pip install django-modeltranslation```
2. Add ```'modeltranslation'``` to ```INSTALLED_APPS```
3. In settings file we have to set ```USE_I18N = True```
4. Add these codes to ```settings.py```

```python
MODELTRANSLATION_DEFAULT_LANGUAGE = "en-us"
MODELTRANSLATION_LANGUAGES = ("en-us", "uz", "ru")
MODELTRANSLATION_FALLBACK_LANGUAGES = ("en-us", "uz", "ru")


def gettext(s):
    return s


LANGUAGES = (
    ("en-us", gettext("English")),
    ("ru", gettext("Русский")),
    ("uz", gettext("O'zbekcha")),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
```

5. Create ```translation.py``` in the app in which we are storing the ```models.py```
6. Add these codes to ```translation.py```

```python
from modeltranslation.translator import translator, TranslationOptions
from .models import Person

# for Person model
class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'profession')

translator.register(Person, PersonTranslationOptions)
```
7. Make migrations and migrate
```python
   python manage.py makemigrations
   python manage.py migrate

```

8. Add to Middleware in ```settings.py```

```python
'django.middleware.locale.LocaleMiddleware',
```

9. Add to ```urls.py```

```python
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
```
10. Create makemesages and compilemessages

```python
python manage.py makemessages -l uz --ignore=venv
python manage.py makemessages -l ru --ignore=venv
python manage.py compilemessages
```