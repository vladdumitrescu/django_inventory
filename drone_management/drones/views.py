from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Drone, CameraBrand
from .forms import DroneForm


# @login_required(login_url="accounts/login")
def show_all_drones(request):
    camera_brand = request.GET.get("camera_brand")

    if camera_brand:
        drones = Drone.objects.filter(camera_brand_filter__name=camera_brand)
    else:
        drones = Drone.objects.order_by("-price")

    page_nb = request.GET.get("page")
    paginator = Paginator(drones, 2)

    try:
        drones = paginator.page(page_nb)
    except PageNotAnInteger:
        drones = paginator.page(1)
    except EmptyPage:
        drones = paginator.page(paginator.num_pages)

    camera_brands = CameraBrand.objects.all()

    context = {
        'drones': drones,
        'camera_brands': camera_brands
    }

    return render(request, 'show_drones.html', context)


def drone_details(request, pk):
    drone_det = Drone.objects.get(id=pk)

    context = {
        'drone_det': drone_det
    }

    return render(request, 'drone_detail.html', context)


def add_drone(request):
    if request.method == 'POST':
        form = DroneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_drones')
    else:
        form = DroneForm()

    context = {
        "form": form
    }

    return render(request, 'add_drone.html', context)


def update_drone(request, pk):
    drone = Drone.objects.get(id=pk)
    form = DroneForm(instance=drone)

    if request.method == "POST":
        form = DroneForm(request.POST, request.FILES, instance=drone)
        if form.is_valid():
            form.save()
            return redirect('show_drones')

    context = {
        "form": form
    }

    return render(request, 'update_drone.html', context)


def delete_drone(request, pk):
    drone = Drone.objects.get(id=pk)
    drone.delete()
    return redirect('show_drones')


def search_bar(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query:
            drones = Drone.objects.filter(name__icontains=query)
            return render(request, "search_bar.html", {"drones": drones})
        else:
            print("No results were found in the database.")
            return render(request, "search_bar.html", {})
