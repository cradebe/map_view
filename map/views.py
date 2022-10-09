from typing import List

import folium
from django.shortcuts import render


# Create your views here.
from user_details.models import Profile


def map_view(request):
    # Create Map Object
    map_object = folium.Map(location=[-30.5595, 22.9375], zoom_start=6)

    # get all user profiles
    user_details: List[Profile] = Profile.objects.all()
    for user_detail in user_details:
        lat, lng = user_detail.getlatlng()
        folium.Marker([lat, lng], tooltip=user_detail.user.get_full_name(), popup=user_detail.get_user_profile()).add_to(map_object)

    context = {'map_object': map_object._repr_html_()}

    return render(request, 'map.html', context)
