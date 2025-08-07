from django.contrib import admin

from .models import Question, Choice

# Create an inline class
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # shows 3 extra blank choice fields by default

# Customize the Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Register your models here.

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

