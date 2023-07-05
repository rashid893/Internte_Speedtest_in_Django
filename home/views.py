from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from speedtest import Speedtest

def speed_test(request):
    speedtester = Speedtest()
    speedtester.download()
    speedtester.upload()
    results = speedtester.results.dict()

    context = {
        'download_speed': results['download'] / 10**6,  # Convert to Mbps
        'upload_speed': results['upload'] / 10**6,  # Convert to Mbps
    }

    return render(request, 'speedtest.html', context)
