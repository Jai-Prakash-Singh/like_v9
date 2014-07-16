from django.contrib import admin
from searchengine.models import sites_table, ip_country, Document

class sites_table_admin(admin.ModelAdmin):
    list_display = ("dimainname", 'image', 'dimainlink', 'status')
    search_fields = ('dimainname', 'dimainlink', 'status')
    list_filter = ('status',)
    date_hierarchy = 'added_date'
    ordering = ('status', 'dimainname',)
    fields = ('dimainname', 'image', 'dimainlink', "imagelink", 'status','added_date' )


admin.site.register(sites_table, sites_table_admin)

class ip_country_admin(admin.ModelAdmin):
    list_display = ('ipfield', 'country', 'keyword', 'added_date')

    fields = ('ipfield', 'country', 'keyword', 'added_date')

admin.site.register(ip_country, ip_country_admin)

class Document_admin(admin.ModelAdmin):
    list_display =('title', 'image', 'urllink', 'status', 'added_date', )
    fields = ('title', 'image', 'urllink', 'status', 'added_date', )


admin.site.register(Document, Document_admin)
