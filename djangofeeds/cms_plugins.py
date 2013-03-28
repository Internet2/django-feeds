from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangofeeds.models import *

class FeedsPlugin(CMSPluginBase):
    model = FeedsPluginModel
    name = _("Feeds")
    render_template = "feeds_plugin.html"
    
    def render(self, context, instance, placeholder):
        feeds = Feed.objects.all()
        if (instance.feeds):
            filters = []
            for tag in instance.tags.split(','):
                filters.append(tag.strip())
            feeds = feeds.filter(name__in = filters).distinct()
        if (instance.tags):
            context['tags'] = instance.tags
            filters = []
            for tag in instance.tags.split(','):
                filters.append(tag.strip())
            feeds = feeds.filter(tags__name__in = filters).distinct()
        else:
            context['tags'] = []
        if feeds.count() > 1:
            filters = []
            for f in feeds:
                 filters.append(f.name.strip())
            posts = Post.objects.filter(feed__name__in = filters).distinct()
        else:
            posts = feeds[0].get_posts()
        posts.order_by("-date_published")
        context['more'] = instance.more
        context['posts'] = posts[:instance.limit]
        return context


plugin_pool.register_plugin(FeedsPlugin)