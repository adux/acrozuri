from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .multiforms import MultiFormsView
from .models import Class
from .forms import RegisterForm, NewsForm


class HomeView(MultiFormsView):
    template_name = "pages/index.html"
    forms_classes = {'register': RegisterForm,
                     'news': NewsForm,
                     }
    success_urls = {'register': reverse_lazy('home'),
                    'news': reverse_lazy('home'),
                    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def register_form_valid(self, form):
        instance = form.save(commit=False)
        form_name = form.cleaned_data.get('action')
        subject = "New Registration"
        message = "Check new registration in www.acrozuri.ch"
        sender = "dontreply@acrozuri.ch"
        to = "info@acrozuri.ch"
        send_mail(subject, message, sender, to)
        instance.save()
        return HttpResponseRedirect(self.get_success_url(form_name))

    def news_form_valid(self, form):
        instance = form.save(commit=False)
        form_name = form.cleaned_data.get('action')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = name + " ," + form.cleaned_data.get('message')
        sender = email
        to = 'info@acrozuri.ch'
        send_mail(subject, message, sender, to)  # TODO config email
        instance.save()
        return HttpResponseRedirect(self.get_success_url(form_name))


class EventView(TemplateView):
    template_name = "pages/event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = Class.objects.all()
        return context
