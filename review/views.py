from django.shortcuts import render
from django.views import generic, View
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review/review.html'

    def get(self, request, *args, **kwargs):
        review_list = Review.objects.filter(status=1)

        return render(
            request,
            "review/review.html",
            {
                "review_list": review_list,
                "review_form": ReviewForm()
            },
        )

    def post(self, request):

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.author = request.user
            review = review_form.save(commit=False)
            review.status = 1
            review.save()
        else:
            review_form = ReviewForm()

        return HttpResponseRedirect('/review')
