from django.shortcuts import render


# route_api/views.py


from django.http import JsonResponse
from utils.fuel_loader import load_fuel_data
from utils.routing_utils import *
from .forms import RouteForm
from django.shortcuts import render
import pandas as pd
import requests


from utils.fuel_utils import *

# route_api/views.py
import openrouteservice
from openrouteservice import convert

# Initialize once with your API key
client = openrouteservice.Client(key='.....')


def route_api(request):
    context = {'form': RouteForm()}

    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']

            try:
                start_coords = geocode_location(origin)
                end_coords = geocode_location(destination)

                route_data = get_route(start_coords, end_coords, 'pk.eyJ1IjoiY29sbG93aGl6IiwiYSI6ImNtYTJiOGZlaDI4aXUycXNtd2wzemlrd2IifQ.HmXd5GcLlbRqnJxU5iQ19g')
                route_coords = route_data['route_geometry']
                total_distance = route_data['distance_km'] * 0.621371

                stop_coords = get_fuel_stops_along_route(route_coords, total_distance)
                fuel_stops = [get_cheapest_station_near(stop, fuel_df) for stop in stop_coords if get_cheapest_station_near(stop, fuel_df)]

                fuel_cost = calculate_total_fuel_cost(total_distance, fuel_stops)
                route_map = generate_route_map(route_coords, fuel_stops)

                context.update({
                    'map': route_map,
                    'fuel_cost': fuel_cost,
                    'origin': origin,
                    'destination': destination
                })

            except Exception as e:
                context['error'] = str(e)

    return render(request, 'fuelroute/route.html', context)


def route_planner_home(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        fuel_df = load_fuel_data()  # load fuel station data

        try:
            route_map_html, total_cost = process_route_and_fuel(origin, destination, fuel_df)
            return render(request, 'fuelroute/route_result.html', {
                'map_html': route_map_html,
                'total_cost': total_cost,
                'origin': origin,
                'destination': destination
            })
        except Exception as e:
            return render(request, 'fuelroute/route_home.html', {'error': str(e)})
    
    return render(request, 'fuelroute/route_home.html')
