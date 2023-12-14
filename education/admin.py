from django.contrib import admin
from education.models import Course, Section, Lesson
from django.utils.html import mark_safe

class SectionInline(admin.TabularInline):
    model = Section

class LessonInline(admin.StackedInline):
    model = Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'level',
                    'course_category', 'lecture' , 'price', 'discount', 'image_tag')
    list_editable = ('title', 'price', 'level', 'lecture' , 'category', 'course_category', 'discount')
    readonly_fields = ['image_tag']
    inlines = [SectionInline]
    list_filter = ["active", "title"]
    
    def image_tag(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100" />')
    

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id','title',)
    list_editable = ('title',)
    inlines = [LessonInline]
    