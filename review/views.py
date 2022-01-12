from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Review


class ReviewListView(ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review/review.html'
    paginate_by = 4

    def get_context(self):
        item = get_object_or_404(Review, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


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


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/delete_review.html'
    success_message = "Review has been deleted"
    success_url = reverse_lazy('review')


class ManageReviewList(generic.ListView):

    model = Review
    queryset = Review.objects.filter(status=0).order_by('-created_on')
    template_name = 'review/manage_reviews.html'


def LikeView(request, pk):
    review = get_object_or_404(Review, id=pk)
    liked = False
    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
        liked = False
    else:
        review.likes.add(request.user)
        liked = True

    return redirect(reverse('review'))


def approvedReview(request, pk):
        review = Review.objects.get(pk=pk)
        review.status = 1
        review.save()
        return HttpResponseRedirect(reverse('manage_review'))
