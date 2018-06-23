from django.contrib import admin

from dialogbot.models import Team, Category


class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'team_id', 'created_on']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on']


admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)
