from django.db.models import Count
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView

from .models import Vote


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
