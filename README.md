# Fuel_Route_Optimizer_API
API for fuel cost estimation and optimized route planning using geospatial data and Django.

# 🚗 Fuel Cost Estimation & Route Optimization API

An end-to-end geospatial API built with **Django** that helps users estimate total fuel costs and optimize routes for long-distance travel using real-time location data, user inputs, and dynamic mapping.

---

## 🔧 Features

- 🗺️ Geocodes start & end locations
- 📍 Places stop points every 500 miles
- ⛽ Identifies cheapest fuel stations near stop points (from uploaded data)
- 📊 Calculates fuel cost based on MPG and fuel prices
- 🌍 Generates interactive route maps using **Folium**
- 🔄 Accepts any fuel station dataset with consistent naming
- 🧱 Built on a clean, scalable **Django REST API** architecture

---

## 🛠️ Tech Stack

- **Backend Framework**: Django (REST Framework)
- **Languages**: Python, HTML, CSS
- **APIs & Libraries**:
  - Mapbox (route data)
  - Nominatim (geocoding)
  - Geopy, Haversine (distance calculations)
  - Pandas (data wrangling)
  - Folium (interactive maps)
  - Mockaroo (synthetic data generation)

---

## 📂 Folder Structure
fuel_api/
├── core/
│ ├── views.py
│ ├── urls.py
│ ├── utils.py
├── templates/
│ └── index.html
├── static/
│ └── styles.css
├── data/
│ └── mock_fuel_stations.csv
├── manage.py
└── README.md




