from django.contrib import admin
from education.models import Course
from django.utils.html import mark_safe

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'level',
                    'course_category', 'price', 'discount', 'image_tag')
    list_editable = ('title', 'price', 'level' , 'category', 'course_category', 'discount')
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100" />')