import datetime
import json

from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views import generic
from weasyprint import HTML

from huscy.consents.forms import SignatureForm
from huscy.consents.models import Consent, ConsentFile


class ConsentView(generic.FormView):
    form_class = SignatureForm
    template_name = 'consents/consent-page.html'

    def dispatch(self, request, *args, **kwargs):
        self.consent = get_object_or_404(Consent, pk=self.kwargs['consent_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['consent'] = self.consent
        return context

    def form_valid(self, form):
        signature = form.cleaned_data.get('signature')
        html_template = get_template('consents/signature-image-template.html')
        rendered_html = html_template.render({
            "consent": self.consent,
            "signature": json.dumps(signature),
            "today": datetime.date.today(),
        })
        content = HTML(string=rendered_html).write_pdf()
        filename = self.consent.name
        f_handle = SimpleUploadedFile(
            name=filename,
            content=content,
            content_type='application/pdf'
        )
        ConsentFile.objects.create(consent=self.consent, filehandle=f_handle)
        return HttpResponse(content, content_type="application/pdf")
