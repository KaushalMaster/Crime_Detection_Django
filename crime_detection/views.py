from django.shortcuts import render
import pyrebase
from datetime import datetime as d
# Create your views here.
config = {
    "apiKey": "AIzaSyAcv7rjtb0TPvaMoRdeqSlUUpiyjjNbioY",
    "authDomain": "realtime-crime-detection-773bc.firebaseapp.com",
    "databaseURL": "https://realtime-crime-detection-773bc-default-rtdb.firebaseio.com",
    "projectId": "realtime-crime-detection-773bc",
    "storageBucket": "realtime-crime-detection-773bc.appspot.com",
    "messagingSenderId": "446675461946",
    "appId": "1:446675461946:web:c2b9e2b657e0932e3dd203"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def index(request):
    return render(request, 'index.html')


def result(request):
    Lattitude = database.child('Cordinates').child('Lattitude').get().val()
    Longitude = database.child('Cordinates').child('Longitude').get().val()
    Accuracy = database.child('Cordinates').child('Accuracy').get().val()
    return render(request, 'result.html', {
        "Lattitude": Lattitude,
        "Longitude": Longitude,
        "Accuracy": Accuracy
    })


def register_complaint(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        complain_type = request.POST.get('Complain_Type')
        complain_description = request.POST.get('complain_description')
        phone = request.POST.get('Phone')
        date = d.now()
        print(full_name, complain_type, complain_description, phone, date)

    return render(request, 'RegisterComplain.html')
