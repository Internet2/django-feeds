from django.contrib import admin

from taggit.models import Tag

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from djangofeeds.models import Feed, Post, Enclosure

class FeedAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        Tag.objects.all().order_by("name"),
        widget=FilteredSelectMultiple("tags", False),
        required=False)

    class Meta:
        model = Feed

class FeedAdmin(admin.ModelAdmin):
    """Admin for :class:`djangofeeds.models.Feed`."""
    list_display = ('name', 'feed_url', 'date_last_refresh', 'is_active')
    search_fields = ['feed_url', 'name']
    form = FeedAdminForm

class PostAdmin(admin.ModelAdmin):
    """Admin for :class:`djangofeeds.models.Post`."""
    list_display = ('title', 'link', 'author', 'date_updated',
                    'date_published')
    search_fields = ['link', 'title']
    date_hierarchy = 'date_updated'

admin.site.register(Enclosure)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Post, PostAdmin)
