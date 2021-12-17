from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


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
    success_message = "Review created, will be approve soon"
    success_url = reverse_lazy('review')

    def getObject(request, id):
        review = get_object_or_404(Review, id=pk)


class ManageReviewList(generic.ListView):

    model = Review
    queryset = Review.objects.filter(status=0).order_by('-created_on')
    template_name = 'review/manage_reviews.html'

    def ApproveReview(request, review_id):
        review_list = Review.objects.filter(status=0)
        review_form = ReviewForm(data=request.POST)

        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=review)
            if form_is_valid():
                review.objects.filter(review_id).update(status=1)
                form.save
                return HttpResponseRedirect('/manage_review')

    def UpdateForm(request, pk):
        form = ReviewForm()
        context = {'form': form}
        return render(request, 'manage_reviews.html', context)


class ApproveReview(generic.ListView):

    queryset = Review.objects.filter(status=0).order_by('-created_on')

    def approveReview(self, request, *args, **kwargs):

        review_id = Review.get_object_or_404(review_id)
        review_form = ReviewForm(data=request.POST)
        review_form.instance.author = request.user
        review = review_form.save(commit=False)
        status = 1
        review.save()

        return HttpResponseRedirect('manage_review')
