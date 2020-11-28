from uuid import uuid4

import accounts.models
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.urls import reverse
from django.utils import timezone
from django_comments.moderation import CommentModerator
from django_comments_xtd.models import XtdComment
from django_comments_xtd.moderation import XtdCommentModerator, moderator
from notifications.signals import notify
from guardian.shortcuts import assign_perm
from django.utils.translation import ugettext as _

from .badwords import badwords


class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset()\
                                         .filter(publish__lte=timezone.now())

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    TYPE_CHOICES = (
        ('assignment', 'Assignment'),
    )
    stream = models.ForeignKey('course.CourseOffering', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    slug = models.UUIDField(default=uuid4, editable=False, unique=True)
    body = models.TextField()
    allow_comments = models.BooleanField('allow comments', default=True)
    publish = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    post_type = models.CharField(_('post type'), max_length=25, blank=True, choices=TYPE_CHOICES)
    assignment = models.ForeignKey('assignment.Assignment', null=True, blank=True, on_delete=models.CASCADE)
    objects = PublicManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.user.username}: {self.body[:30]}'

    def get_absolute_url(self):
        return reverse('course:stream:post-detail', kwargs={ 'slug': self.stream.slug, 'post_slug': self.slug })

def post_save_handler(sender, instance, created, **kwargs):
    users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.stream)

    # add permission to teacher, so only teacher can edit and view this assignment

    if created:
        # add all permssion to student
        assign_perm('add_post', instance.user, instance)
        assign_perm('change_post', instance.user, instance)
        assign_perm('delete_post', instance.user, instance)
        assign_perm('view_post', users, instance)

        # permission for teacher
        assign_perm('delete_post', instance.stream.teacher.user, instance)
        assign_perm('view_post', instance.stream.teacher.user, instance)

        description = f'posted in { instance.stream.course.code }'
        href = instance.get_absolute_url()
        
        if instance.user.is_student:
            # to teacher
            notify.send(instance.user, verb='posted', recipient=instance.stream.teacher.user, action_object=instance, target=instance.stream, description=description, href=href)

            # to all students excepts current sender
            notify.send(instance.user, verb='posted', recipient=users.exclude(id=instance.user.id), action_object=instance, target=instance.stream, description=description, href=href)

        if instance.user.is_teacher:
            # to all students
            notify.send(instance.user, verb='posted', recipient=users, action_object=instance, target=instance.stream, description=description, href=href)

post_save.connect(post_save_handler, sender=Post)

class PostCommentModerator(XtdCommentModerator):
    email_notification = True
    removal_suggestion_notification = True

moderator.register(Post, PostCommentModerator)
