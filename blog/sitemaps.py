from django.contrib.sitemaps import Sitemap
from jobs.models import posts


class PostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return posts.objects.all()

    def lastmod(self, obj):
        return obj.timestamp



#tanehs
