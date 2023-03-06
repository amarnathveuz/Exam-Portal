from django.contrib import admin

# Register your models here.

from .models import  *


admin.site.register(Main_Exam_section)
admin.site.register(Main_Exam_Master)
admin.site.register(Main_Question_Bank)
admin.site.register(Question_Bank_multiple_choice)
admin.site.register(Section_Question_Mapping)


admin.site.register(Exam_inital_field)
admin.site.register(Exam_inital_field_choice)



