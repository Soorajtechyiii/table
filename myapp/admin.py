from django.contrib import admin
from.models import student
class html(admin.ModelAdmin):
    list_display=('name','place','phonenumber','qualification','fathersname','mothersname','experience')
admin.site.register(student,html)

