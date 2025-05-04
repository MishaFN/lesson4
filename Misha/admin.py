from django.contrib import admin

from .models import News,Category


admin.site.register(Category)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
        list_display=('title','pub_date','category')