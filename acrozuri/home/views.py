from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .multiforms import MultiFormsView
from .models import Class
from .forms import MemberForm, NewsForm


class HomeView(MultiFormsView):
    template_name = "pages/index.html"
    form_classes = {'news': NewsForm}
    success_urls = {'news': reverse_lazy('home')}

    def news_form_valid(self, form):
        instance = form.save(commit=False)
        form_name = form.cleaned_data.get('action')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = name + " ," + form.cleaned_data.get('message')
        sender = email
        to = 'info@acrozuri.ch'
        send_mail(subject, message, sender, to)
        instance.save()
        return HttpResponseRedirect(self.get_success_url(form_name))


class EventView(TemplateView):
    template_name = "pages/event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = Class.objects.all()
        return context


class MemberView(FormView):
    template_name = "pages/form.html"
    form_class = MemberForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        subject = "Verein Registration"
        message = "Thanks for Registering" + instance.first_name + ' ' + instance.last_name + " we will get in contact with you in the next 3 working days. \r\n\r\n See you soon\r\nAcro Züri Verein"
        sender = "noreply@acrozuri.ch"
        to = {instance.email, 'info@acrozuri.ch'}
        send_mail(subject, message, sender, to)
        instance.save()
        return super().form_valid(form)
