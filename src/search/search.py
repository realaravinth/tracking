from django.db import models
from .models import Search,Results,Location
from signal_sort.models import Signal_sort
from signal_sort.signal_sort import signal_sort
from tracker_registration.models import Tracker_register
from beacon.models import Beacon
from signal_sort.models import Signal_sort

def search_matches(search):
    # Signal_sort.objects.all().delete()
    
    # search=Search.objects.last()
    tracker=Tracker_register.objects.latest('id')
    status="not found"
    for x in range(tracker.id,0,-1):
        tracker_match=Tracker_register.objects.get(id=x)
        if tracker_match.tracker_number==search['employee_num']:
            status="found"
    if status=="found":
        a=signal_sort(search)
        # loopUpperControl=Signal_sort.objects.last()
        # loopLowerControl=Signal_sort.objects.first()
        # for i in range(loopUpperControl.id,loopLowerControl.id,-1):
        #     stored_location=Signal_sort.objects.get(id=i)
        #     if search['employee_num']==stored_location.employee_num:
        #         status=stored_location.bssid
        process_location(a)      
        #        break
    
    return status

def process_location(x):
    
    beacon=Beacon.objects.last()
    for i in range(beacon.id,0,-1):
        obj=Beacon.objects.get(id=i)
        
        if x==obj.beacon_name:
            Location.objects.create(room=obj.room,floor=obj.floor)
                    
        
    