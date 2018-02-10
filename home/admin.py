from django.contrib import admin
from .models import Team
from .models import Player
from .models import Golfers

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.


#class ProfileInline(admin.StackedInline):
#    model = Player
#    can_delete = False
#    verbose_name_plural = 'Total Winnings'
#    fk_name = 'user'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    model = Player
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','get_team')
#    list_select_related = ('player', )
#
    def get_team(self, instance):
        return instance.player.name
    get_team.short_description = 'Team'
#
#    def get_inline_instances(self, request, obj=None):
#        if not obj:
#            return list()
#        return super(UserAdmin, self).get_inline_instances(request, obj)
#
#    def get_inline_instances(self, request, obj=None):
#        if not obj:
#            return list()
#        return super(UserAdmin, self).get_inline_instances(request, obj)


#class PlayereInline(admin.StackedInline):
#    model = Player
#    can_delete = False
#    extra = 0


class ProfileInline(admin.StackedInline):
    model = Golfers
    extra = 2

class PlayerAdmin(admin.ModelAdmin):
    model = Golfers
    inlines = (ProfileInline, )
    list_display = ('name', 'memberone','membertwo','score')


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
    #        return super(UserAdmin, self).get_inline_instances(request, obj)










admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team, PlayerAdmin)
