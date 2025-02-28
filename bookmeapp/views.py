from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Slot,Availability
import json

def home(request):
    slots = Slot.objects.all()
    return render(request, "slot.html", {"slots": slots})

@csrf_exempt
def save_availability(request):
    if request.method == "POST":
        data = json.loads(request.body)
        for entry in data:
            date = entry["date"]
            status = entry["status"]
            color = entry["color"]

            availability, created = Availability.objects.update_or_create(
                date=date,
                defaults={"status": status, "color": color}
            )

        return JsonResponse({"message": "Availability saved successfully!"})

    return JsonResponse({"error": "Invalid request"}, status=400)


def get_availability(request):
    data = list(Availability.objects.values("date", "status", "color"))
    return JsonResponse(data, safe=False)

