from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
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
        message = "From: " + email + "\r\nName:" + name + " \r\n\r\nMessage: " + form.cleaned_data.get('message')
        sender = 'noreply@acrozuri.ch'
        to = ['info@acrozuri.ch']
        send_mail(subject, message, sender, to)
        messages.add_message(self.request, messages.SUCCESS, F'Thanks for writing us, we will get back to you ;) !')
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
        # TODO make a template email function
        instance = form.save(commit=False)
        subject = "Acro Zuri Verein - Registration"
        message = "Grüessech " + instance.first_name + " " + instance.last_name + "\r\n\r\n Thanks for registering! We will get in touch within the next days.\r\n\r\nTo get the latest news of the Verein register to our mailing list: http://eepurl.com/dKx6Ns\r\n\r\nSee you soon!\r\nAcro Züri Verein"
        sender = 'noreply@acrozuri.ch'
        to = [instance.email, 'info@acrozuri.ch']
        send_mail(subject, message, sender, to)
        instance.save()
        messages.add_message(self.request, messages.SUCCESS, F'Thanks for Registering, please check your email.')
        return super().form_valid(form)
