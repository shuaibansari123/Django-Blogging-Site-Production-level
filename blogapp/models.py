
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT, SET_DEFAULT, SET_NULL
import uuid
# Create your models here.
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    first_name=models.CharField(max_length=255 , blank=True , null=True)
    last_name = models.CharField(max_length=255 , blank=True , null=True)
    full_name = models.CharField(max_length=255 , blank=True)
    unique_id = models.UUIDField(  default=uuid.uuid4 , unique=True , editable=False )
    email = models.EmailField(default="AnonymousEmailId")
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' , 'password' , ]

    #objects = CustomUserManager()

    def __str__(self):
        return self.username




class Blog(models.Model):
    video_blog= models.FileField(upload_to='my_videos' , blank=True , null=True)
    #create_by = models.ForeignKey(User ,on_delete=SET_DEFAULT ,  default="Anonymos"  , related_name='create_by')
    cat = ( ('BIO-GRAPHY' , 'BIO-GRAPHY') , ('cricket' , 'cricket'),('technical' , 'technical') , ('invensions' , "invensions") , ('others' , 'others'))
    #post_category = models.CharField(choices=cat , default="BIO-GRAPHY" , max_length=25)
    created_time = models.DateTimeField(auto_now_add=True)
    #like = models.IntegerField(default=0)
    main_image = models.ImageField(upload_to='images/shop' , blank=True)
    main_title = models.CharField(max_length=3000  , default='BIO-GRAPHY')
    pera_1=  RichTextField()
    like_blog = models.ManyToManyField( User  , blank=True  )

    

    def __str__(self):
        return f" CREATED-BY---{self.created_time} ---{self.main_title}"
    
#obj_custom = User.objects.get(username='shuaib2@gmail.com')
class Comment(models.Model):
    comment_for = models.ForeignKey(Blog , on_delete=models.CASCADE )
    comment_text =  models.TextField(max_length=1100)
    comment_created_by = models.ForeignKey(User , on_delete=models.CASCADE ,blank=True)
    comment_created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"-KISNE--{self.comment_created_by} ----- KIS-BLOG PE -{self.comment_for}[:10]- KARA HAI "




class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.IntegerField(blank=True , null=True )
    message =  models.TextField(max_length=2000)

    def __str__(self):
        return str(self.name)



'''
class Likes(models.Model):
    like_id = models.UUIDField(primary_key=True , default=uuid.uuid4 , unique=True , editable=False)
    like_for = models.OneToOneField(Blog , on_delete=PROTECT  , blank=True)
    #like_person = models.ManyToManyField(User ,  default="" , blank=True) 
    like_time = models.DateTimeField(auto_now_add=True)
    total_like = models.IntegerField(default=0)

    def __str__(self):
        return f"{str(self.total_like)} {self.like_for}"



class Unique_user(models.Model):
    unique = models.UUIDField(default=uuid.uuid4  , unique=True , editable=False)
    name = models.CharField( blank=False , null=False , max_length=255)

    def __str__(self):
        return self.unique
'''











