from django.db import models
from .models import Location
from getdata.models import Cleaned
from tracker_registration.models import Tracker_register
from beacon.models import Beacon


def search_matches(search):
    tracker=Tracker_register.objects.latest('id')
    status="not found"
    for x in range(tracker.id,0,-1):
        tracker_match=Tracker_register.objects.get(id=x)
        if tracker_match.tracker_number==search['employee_number']:
            status="found"
    if status=="found":
        process_location(find_match(search))      
    return status

def find_match(search):
    count=0
    ids="0 "
    possible=Cleaned.objects.filter(employee_number=search)
    for a in possible:
        count+=1
        ids+=str(a.id)+' '
    ids=ids.split()
    stronger=Cleaned.objects.last()
    for i in range (count,0,-2):
        a=Cleaned.objects.get(id=ids[i])
        b=Cleaned.objects.get(id=ids[i-1])
        stronger=b
        if a.signal_strength>b.signal_strength:
            stronger=a
    return stronger.ssid

def process_location(x):
    beacon=Beacon.objects.last()
    for i in range(beacon.id,0,-1):
        obj=Beacon.objects.get(id=i)
        
        if x==obj.beacon_name:
            Location.objects.create(room=obj.room,floor=obj.floor)
            print(obj)
                    
        
    