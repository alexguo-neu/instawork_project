from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import PeopleModelForm
from .models import People
from django.views import View
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'teams/index.html'
    model = People


class DetailView(generic.DetailView):
    model = People
    template_name = 'teams/detail.html'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            # GET method
            form = PeopleModelForm(instance=obj)
            context = {"form": form}
            context['object'] = obj
        return render(request, self.template_name, context)
    def post(self, request, id=None, *args, **kwargs):
        # POST method
        people = self.get_object()
        if (request.POST):
            if 'edit' in request.POST:
                if people is not None:
                    form = PeopleModelForm(request.POST, instance=people)
                    if form.is_valid():
                        form.save()
            elif 'del' in request.POST:
                if people is not None:
                    people.delete()
        return HttpResponseRedirect(reverse('teams:index'))

class createView(View):
    template_name = "teams/add.html"  # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = PeopleModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        # POST method
        form = PeopleModelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('teams:index'))


