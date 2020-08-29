from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import FormView, CreateView
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView

from .forms import VotingForm
from .models import Vote


class VotingView(CreateView):
    form_class = VotingForm
    template_name = 'vote.html'
    success_url = '/polls/view'

    def get_context_data(self, **kwargs):
        data = super(VotingView, self).get_context_data(**kwargs)
        try:
            data['polls'] = Vote.objects.values('design_id').annotate(votes=Count('design_id')).order_by('design_id')
        except KeyError:
            data['polls'] = {}
        data['vote_count'] = Vote.objects.values('design_id').count()
        return data


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
