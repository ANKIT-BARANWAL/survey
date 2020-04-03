from django.contrib import admin

# Register your models here.
from .models import Survey
from .models import Question
from .models import Choice
from .models import QuestionAnswer
from .models import SurveyAnswer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuestionAnswer)
admin.site.register(SurveyAnswer)