from django.db import models
from .models import Search,Results
from signal_sort.models import Signal_sort
from signal_sort.signal_sort import signal_sort
from tracker_registration.models import Tracker_register
from beacon.models import Beacon
from signal_sort.models import Signal_sort

def search_matches():
    a=signal_sort()
    search=Search.objects.last()
    tracker=Tracker_register.objects.latest('id')
    status="not found"
    for x in range(tracker.id,0,-1):
        tracker_match=Tracker_register.objects.get(id=x)
        if tracker_match.tracker_number==search.employee_num:
            status="found"
        # if tracker_match.employee_num!=search.employee_num:

    if status=="found":
        loopUpperControl=Signal_sort.objects.last()
        loopLowerControl=Signal_sort.objects.first()
        for i in range(loopUpperControl.id,loopLowerControl.id,-1):
            stored_location=Signal_sort.objects.get(id=i)
            if search.employee_num==stored_location.employee_num:
                status=process_location(stored_location.bssid)
    return status

def process_location(x):
    beacon=Beacon.objects.last()
    for i in range(beacon.id,0,-1):
        obj=Beacon.objects.last()
        if x==obj.beacon_name:
            return obj        
        
    