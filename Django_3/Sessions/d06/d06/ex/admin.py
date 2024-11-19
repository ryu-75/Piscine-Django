from django.contrib import admin
from ex.models import Users, Tip
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class CustomAdmin(admin.ModelAdmin):
    list_display = ('username', 'reputation', 'is_superuser', 'is_staff', 'is_active')
    
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    
    search_fields = ('username', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')})
    )
    actions = ['can_delete_tip', 'cannot_delete_tip', 'add_downvoted_tip', 'not_add_downvoted_tip']
    
    # Permission to delete a tip
    def can_delete_tip(self, request, queryset):
        permission = Permission.objects.get(codename='auth_delete_tip')
        for user in queryset:
            user.user_permissions.add(permission)                
        self.message_user(request, "You have permission to delete a tip")
    can_delete_tip.short_description = "Given permission to delete a tip or not"
    
    def cannot_delete_tip(self, request, queryset):
        permission = Permission.objects.get(codename='auth_delete_tip')
        for user in queryset:
            user.user_permissions.remove(permission)                
        self.message_user(request, "You don't have permission to delete a tip")
    cannot_delete_tip.short_description = "Remove permission to delete a tip or not"
    
    # Permission to add a downvote
    def add_downvoted_tip(self, request, queryset):
        permission = Permission.objects.get(codename='can_add_downvote')
        for user in queryset:
            user.user_permissions.add(permission)
        self.message_user(request, "You have permission to add a downvote")
    add_downvoted_tip.short_description = "Given permission to add a downvote or not"
    
    def not_add_downvoted_tip(self, request, queryset):
        permission = Permission.objects.get(codename='can_add_downvote')
        for user in queryset:
            user.user_permissions.remove(permission)
        self.message_user(request, "You don't have permission to add a downvote...")
    not_add_downvoted_tip.short_description = "Remove permission to add a downvote or not"
    
admin.site.register(Users, CustomAdmin)