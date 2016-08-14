from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import InterestedUser

# Create your views here.


class InterestedUserCreate(CreateView):
    model = InterestedUser
    fields = ['email']
    template_name = "comingsoon/index.html"
    success_url = 'thanks'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(InterestedUserCreate, self).form_valid(form)


# def thanks(request):
#     return redirect('comingsoon/thanks.html')
