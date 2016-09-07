from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import WorkPluginModel


class WorkPlugin(CMSPluginBase):
    model = WorkPluginModel
    name = _("Work Tile")
    render_template = "work/work_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(WorkPlugin)

