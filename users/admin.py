from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
#admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','phone_number','website','picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website','picture')
    search_fields = ('user__email','user__first_name','user__last_name')
    list_filter = ('created','modified','user__is_active')
    
    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra Info',{
            'fields':(
                ('phone_number','website'),
                ('biography',)
            )
        }),
        ('Metadata',{
            'fields':(
                ('created','modified'),
            )
        })
    )
    
    readonly_fields = ('created','modified','user')
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)