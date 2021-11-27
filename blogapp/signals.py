'''from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from .models import Blog , User, Likes , Unique_user

@receiver(post_save, sender=Blog)
def create_customer(sender, instance, created, **kwargs):
    if created:
        
        custom= User.objects.get(username='anon')
        print(custom  , instance , instance.create_by)
        like_obj = Likes.objects.create(like_for=instance)
        
        like_obj.save()


@receiver(post_save, sender=Blog)
def create_customer(sender, instance, created, **kwargs):
    if created:
        
        custom= User.objects.get(username='anon')
        print(custom  , instance , instance.create_by)
        like_obj = Likes.objects.create(like_for=instance)
        
        like_obj.save()
        '''