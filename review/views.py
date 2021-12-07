from django.shortcuts import render
from django.views import generic, View
from .models import Review
from .forms import ReviewForm


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'review/review.html'


# class CreateReview(View):

#     def get(self, request):

#         review_form = ReviewForm(data=request.POST)

#         return render(
#             request,
#             'review/review.html',
#             {
#                 "review": review,
#                 "review_form": ReviewForm()
#             },
#         )

#     def post(self, request):

#         review_form = ReviewForm(data=request.POST)

#         if review_form.is_valid():
#             review_form.instance.name = request.user.username
#             review = review_form.save(commit=False)
#             review.save()
#         else:
#             review_form = ReviewForm()

#         return render(
#             request,
#             'review/review.html',
#             {
#                 "review": review,
#                 "review_form": ReviewForm()
#             },
#         )