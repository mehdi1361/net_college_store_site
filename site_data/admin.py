from django.contrib import admin
from site_data.models import Slider, Category, CourseCategory
from django.utils.html import mark_safe

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'text', 'image_tag')
    list_editable = ('title', 'text')
    readonly_fields = ['image_tag']
    
    
    def image_tag(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100" />')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "image_tag", "active")
    list_editable = ('name', "active")
    
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="22" />')


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',  'color', 'image_tag', "active")
    list_editable = ("color", "active")
    readonly_fields = ['image_tag']
    
    def image_tag(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="32" height="32" />')


