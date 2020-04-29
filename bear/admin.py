from django.contrib import admin

# Register your models here.
from bear.models import Stu_info, Question_info, Tec_info

admin.site.register(Stu_info)
admin.site.register(Tec_info)
admin.site.register(Question_info)
