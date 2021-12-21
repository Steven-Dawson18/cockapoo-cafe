from .models import Reservation


def get_notification(request):
    """
    Function that count new reservations
    """
    count = Reservation.objects.filter(accepted=True).count()
    data = {
        "count": count
    }
    return data
