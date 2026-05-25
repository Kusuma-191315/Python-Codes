from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
def thankyou(request):
    return HttpResponse("ThankYou Mr/Ms Django!")
    