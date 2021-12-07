from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView
# from myapp.models import Author


# class AuthorCreate(LoginRequiredMixin, CreateView):
#     model = Author
#     fields = ['name']

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)


def reservation(request):
    return render(request, "reservation/reservation.html")
