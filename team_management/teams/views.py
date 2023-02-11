from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import PeopleModelForm
from .models import People
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'teams/index.html'
    model = People


class DetailView(generic.DetailView):
    model = People
    template_name = 'teams/detail.html'

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

