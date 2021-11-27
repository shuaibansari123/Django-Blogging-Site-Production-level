from django.contrib import admin
from .models import Comment, User, Blog   , Contact#,Likes  #, Simple_user
from django.contrib.auth.admin import UserAdmin 
#from django.contrib.auth.models import User
from django.utils.html import format_html
from django.contrib import messages


def super_users(modeladmin , request , quaryset):
    print(modeladmin)
    print(quaryset)
    print(request)
    quaryset.update(is_superuser = True)
super_users.dispcription = 'Make Super User'

def not_super_users(modeladmin , request , quaryset):
    print(modeladmin)
    print(quaryset)
    print(request)
    quaryset.update(is_superuser = False)
not_super_users.dispcription = 'DELETE Super User'


#def move_proxy_model(modeladmin , request , quaryset):
    
    #for i in quaryset:
        #obj=Simple_user.objects.create(name=i.username ,  status='processing' )
    
#move_proxy_model.dispcription = 'move_proxy_model User'



class UserAdmin(UserAdmin):
    model = User
    list_display = ['email' , 'is_superuser', 'full_name' , 'less_content' , 'unique_id']
    list_display_links = ['less_content' , 'email']
    list_filter = ['email' ,  'is_superuser', 'username' , 'date_joined']
    fieldsets = (
       ( 'Required Fields ' , {'fields' : ( 'email' , 'password') }  ),
       
       ( 'Permission Fields ' , {'fields' :( ('full_name' , 'is_staff' , 'username') ,('is_superuser' , 'is_active') , ) }  ),
       
       ( 'Important Dates ' , {'fields' : ('last_login' , 'date_joined') }  ) , 
       ('Advanced options' ,{
               'classes':('collapse' , ) ,
               'fields' :('user_permissions' , 'groups' , ) ,
           
           }), 
    )
    
    # for  add objects page of the model in django admin site   
    add_fieldsets = (
        (  'Add User Object ' , {
            'classes':('wide' , ) , #class for css
            'fields':{'email' , 'full_name' , 'password1'  , 'password2' , 'username' ,  'is_staff' , 'is_active' , 'is_superuser' ,}
        }) , 
       )
    search_fields =('email' ,)
    ordering = ('email', )
    actions=[super_users , not_super_users ]

    def less_content(self , obj):
        return format_html(f'<a>{obj.email}</a>')
    

#admin.autodiscover()
admin.site.register(User , UserAdmin)
admin.site.register(Blog)
admin.site.register(Comment)

admin.site.register(Contact)
#admin.site.register(Simple_user)

        
#admin.site.unregister(User)

        
'''

class LikeAdmin(admin.ModelAdmin):
    model = Likes
    list_display = ['like_id' , 'like_for', 'like_time' , 'total_like']
    fieldsets = (
       ( 'Required Fields ' , {'fields' : ( 'like_for' , 'total_like') }  ),
       
       
       #( 'Important Dates ' , {'fields' : ('like_time' ) }  ) , 
       
    )
    
    # for  add objects page of the model in django admin site   
   
admin.site.register(Likes ,  LikeAdmin) '''