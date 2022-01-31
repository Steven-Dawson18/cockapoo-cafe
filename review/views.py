'''Review views'''
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review


def error_404_view(request, exception):
    return render(request, '404.html')


class ReviewListView(ListView):
    '''
    View to show the reviews that have been made
    Logged in user can only edit or delete their review but can see all
    reviews even if not logged in.
    '''
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review/review.html'
    paginate_by = 4

    def get_context(self):
        '''
        Function gives the user the ability to like a review.
        '''
        item = get_object_or_404(Review, id=self.pk)
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    View displays the form to create a review to the user.
    They must be logged in to make a review and will receive a message
    of success when submitted. The review must be accepted before it will
    visible on the review page.
    '''
    model = Review
    fields = ['title', 'body', 'image']
    template_name = 'review/create_review.html'
    success_message = "Review created, will be approve soon"
    success_url = '/review/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    View displays the form to update a review to the user.
    They must be logged in to update a review and will receive a message
    of success when submitted. The user will only be able to update their
    own review.
    '''
    model = Review
    fields = ['title', 'body', 'image']
    template_name = 'review/update_review.html'
    success_message = "Review has been updated"
    success_url = reverse_lazy('review')

    def get(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        return super(ReviewUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        review = Review.objects.get(pk=pk)
        review.status = 0
        review.save()
        messages.success(request, 'The Review has been sent for approval.')
        return super(ReviewUpdateView, self).post(request, *args, **kwargs)


class ReviewDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''
    View displays the option to delete the review to the user.
    '''
    model = Review
    template_name = 'review/delete_review.html'
    success_message = "Review has been deleted"
    success_url = reverse_lazy('review')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReviewDeleteView, self).delete(request, *args, **kwargs)


class ManageReviewList(generic.ListView):
    '''
    View displays a list of reviews that need to be either accepted
    or rejected.
    '''
    model = Review
    queryset = Review.objects.filter(status=0).order_by('-created_on')
    template_name = 'review/manage_reviews.html'


def like_view(request, pk):
    '''
    Function gives the user the ability to like a review.
    '''
    review = get_object_or_404(Review, id=pk)
    liked = False
    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
        liked = False
    else:
        review.likes.add(request.user)
        liked = True

    return redirect(reverse('review'))


def approved_review(request, pk):
    '''
    Function gives the admin the ability to approve a review.
    '''
    review = Review.objects.get(pk=pk)
    review.status = 1
    review.save()
    messages.success(request, 'The Review has been approved.')
    return HttpResponseRedirect(reverse('manage_review'))
