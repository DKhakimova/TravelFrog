from django.shortcuts import render, redirect, HttpResponse
from log_reg_app.models import User
from . models import Trip, Plan
from django.contrib import messages


# Create your views here.

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'trips.html', context)

def new_trip(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'new_trip.html', context)

def create_trip(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        errors = Trip.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard/trip/new')

        trip = Trip.objects.create(
            destination = request.POST['destination'],
            description = request.POST['description'],
            creator = User.objects.get(id=request.session['user_id'])    
        )
    return redirect('/dashboard')

def edit_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
            'user': User.objects.get(id=request.session['user_id']),
            "trip": Trip.objects.get(id=trip_id)
        }
    return render(request, 'edit_trip.html', context)

def show_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    trip = Trip.objects.get(id=trip_id)
    trip_plan_ids = []
    for plan in trip.trip_plans.all():
        trip_plan_ids.append(plan.id)
    plan_type_filter = "All"
    if request.method == "POST" and request.POST['plan_type'] and request.POST['plan_type'] != "All":
        plan_type_filter = request.POST['plan_type']
        all_plans = Plan.objects.exclude(id__in=trip_plan_ids).filter(destination=trip.destination).filter(plan_type=plan_type_filter)
    else:
        all_plans = Plan.objects.exclude(id__in=trip_plan_ids).filter(destination=trip.destination)


    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'trip': trip,
        'all_plans': all_plans,
        'plan_type_filter': plan_type_filter
    }
    return render(request, 'trip_details.html', context)

def update_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        errors = Trip.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/dashboard/trip/edit/{trip_id}')

        trip = Trip.objects.get(id=trip_id)
        trip.destination = request.POST['destination']
        trip.description = request.POST['description']
        trip.save()
    return redirect('/dashboard')

def remove_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    Trip.objects.get(id=trip_id).delete()
    return redirect('/dashboard')

def new_plan_for_trip(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'trip_id': trip_id
    }
    return render(request, 'new_plan.html', context)

def create_plan(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        errors = Plan.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard/plan/new')

    if request.method == "POST":
        plan = Plan.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            destination = request.POST['destination'],
            plan_type = request.POST['plan_type'],
            creator = User.objects.get(id=request.session['user_id'])    
        )
        trip_id = request.POST['trip_id']
        if(trip_id):
            trip = Trip.objects.get(id = request.POST['trip_id'])
            if(trip):
                plan.trips_with_plan.add(trip)
                return redirect(f"/dashboard/trip/{trip.id}")

    return redirect("/dashboard")

def add_plan(request, plan_id):
    if request.method == "POST":
        plan = Plan.objects.get(id = plan_id)
        trip = Trip.objects.get(id = request.POST['trip_id'])
        plan.trips_with_plan.add(trip)
    return redirect(f"/dashboard/trip/{trip.id}")
    
def remove_plan(request, plan_id):
    if request.method == "POST":
        plan = Plan.objects.get(id = plan_id)
        trip = Trip.objects.get(id = request.POST['trip_id'])
        plan.trips_with_plan.remove(trip)
    return redirect(f"/dashboard/trip/{trip.id}")

def new_plan(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'new_plan.html', context)

def edit_plan(request, plan_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        "plan": Plan.objects.get(id=plan_id)
    }
    return render(request, 'edit_plan.html', context)

def update_plan(request, plan_id):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        errors = Plan.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/dashboard/plan/edit/{plan_id}')

        plan = Plan.objects.get(id=plan_id)
        plan.name = request.POST['name']
        plan.description = request.POST['description']
        plan.destination = request.POST['destination']
        plan.plan_type = request.POST['plan_type']
        plan.creator = User.objects.get(id=request.session['user_id'])
        plan.save()
    return redirect('/dashboard')

def delete_plan(request, plan_id):
    if 'user_id' not in request.session:
        return redirect('/')

    plan = Plan.objects.get(id=plan_id)
    user = User.objects.get(id=request.session['user_id'])
    if user == plan.creator:
        plan.delete()
    return redirect('/dashboard')