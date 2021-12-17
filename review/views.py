from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Review


class ReviewListView(ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review/review.html'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'body', 'image']
    template_name = 'review/create_review.html'
    success_message = "Review created, will be approve soon"
    success_url = '/review/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['title', 'body', 'image']
    template_name = 'review/update_review.html'
    success_message = "Review has been updated"
    success_url = reverse_lazy('review')


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/delete_review.html'
    success_message = "Review has been deleted"
    success_url = reverse_lazy('review')


class ManageReviewList(generic.ListView):

    model = Review
    queryset = Review.objects.filter(status=0).order_by('-created_on')
    template_name = 'review/manage_reviews.html'
