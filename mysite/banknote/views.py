from django.views.generic import DetailView

from banknote import UNDISPLAY_APPRAISAL_FIELDS
from banknote.models import Appraisal


class AppraisalDetail(DetailView):
    model = Appraisal
    context_object_name = 'appraisal'
    template_name = 'banknote/appraisal_detail.html'

    slug_field = 'id_num'
    slug_url_kwarg = 'id_num'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        field_names = [f.name for f in Appraisal._meta.get_fields()]
        for x in UNDISPLAY_APPRAISAL_FIELDS:
            field_names.remove(x)
        context['field_names'] = field_names
        return context
