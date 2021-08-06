from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from posts.models import Post


# Register your models here.
#admin.site.register(Profile)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    """list_display = ('pk','user','phone_number','website','picture')
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
    
    readonly_fields = ('created','modified','user')"""