from django.db import transaction
from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import FormView, CreateView, View
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView

from .forms import VotingForm
from .models import Vote


class VotingView(View):
    model = Vote
    template_name = 'vote.html'
    
    
    def context_data(self, **kwargs):
       data = kwargs
       try:
           data['polls'] = Vote.objects.values('design_id').annotate(votes=Count('design_id')).order_by('design_id')
       except KeyError:
           data['polls'] = {}
       data['vote_count'] = Vote.objects.values('design_id').count()
       return data


    def get(self, request, *args, **kwargs):
        form = VotingForm()
        return render(request, 'vote.html', self.context_data(form=form))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = VotingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            vote = form.save()

            return redirect('/polls/vote-submitted')
            
        return render(request, 'vote.html', self.context_data(form=form))

    
    #form_class = VotingForm
    #template_name = 'vote.html'
    #success_url = '/polls'

    #def get_context_data(self, **kwargs):
    #    data = super(VotingView, self).get_context_data(**kwargs)
    #    try:
    #        data['polls'] = Vote.objects.values('design_id').annotate(votes=Count('design_id')).order_by('design_id')
    #    except KeyError:
    #        data['polls'] = {}
    #    data['vote_count'] = Vote.objects.values('design_id').count()
    #    return data


class ListCreateVote(ListCreateAPIView):
    model = Vote
    queryset = Vote.objects.all()

    def get(self, request, *args, **kwargs):
        # if request.user.is_anonymous:
        #     return JsonResponse({"status": False, "message": "Login required to see entries"}, status=401)
        # if not request.user.is_staff:
        #     return JsonResponse({"status": False, "message": "Staff login required to see entries"}, status=403)
        return super(ListCreateVote, self).get(request, *args, **kwargs)


class Poll(APIView):

    def get(self, request):
        poll = Vote.objects.values('design_id').annotate(votes=Count('design_id')).order_by('votes')
        # ttodo: return json of vootes
        return JsonResponse({"poll": "Compleeted"})
