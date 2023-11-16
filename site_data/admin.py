from django.contrib import admin
from site_data.models import Slider, Category
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
    list_display = ('id', 'name', )
    list_editable = ('name',)

