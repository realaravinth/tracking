from getdata.models import Scan
from search.models import Search,Results
from signal_sort.models import Signal_sort
from sort.models import Sorted

def delete_all():
    Scan.objects.all().delete()
    # Search.objects.all().delete()
    # Results.objects.all().delete()
    Signal_sort.objects.all().delete()
    # Sorted.objects.all().delete()
