from django.contrib import admin
from home.models import Subscriber, Campaign

# Register your models here.
admin.site.register(Subscriber)
#admin.site.register(Campaign)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('subject', 'published_date')