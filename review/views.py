from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review/review.html'

    # def get(self, request, *args, **kwargs):
    #     review_list = Review.objects.filter(status=1)

    #     return render(
    #         request,
    #         "review/review.html",
    #         {
    #             "review_list": review_list,
    #             "reviewed": False,
    #             "review_form": ReviewForm()
    #         },
    #     )

    # def post(self, request):

    #     review_list = Review.objects.filter(status=1)
    #     review_form = ReviewForm(data=request.POST)

    #     if review_form.is_valid():
    #         review_form.instance.author = request.user
    #         review = review_form.save(commit=False)
    #         review.save()

    #         return render(
    #         request,
    #         "review/review.html",
    #         {
    #             "review_list": review_list,
    #             "reviewed": True,
    #             "review_form": ReviewForm()
    #         },
    #     )
    #     else:
    #         review_form = ReviewForm()

    #     return HttpResponseRedirect('/review')


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


class CreateReview(generic.ListView):

    model = Review
    # queryset = Review.objects.filter(status=0).order_by('-created_on')
    template_name = 'review/create_review.html'

    def get(self, request, *args, **kwargs):
        review_list = Review.objects.filter(status=1)

        return render(
            request,
            "review/create_review.html",
            {
                "review_list": review_list,
                "reviewed": False,
                "review_form": ReviewForm()
            },
        )

    def post(self, request):

        review_list = Review.objects.filter(status=1)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.author = request.user
            review = review_form.save(commit=False)
            review.save()

            return render(
            request,
            "review/review.html",
            {
                "review_list": review_list,
                "reviewed": True,
                "review_form": ReviewForm()
            },
        )
        else:
            review_form = ReviewForm()

        return HttpResponseRedirect('/review')

    # def updateReview(request):
        
