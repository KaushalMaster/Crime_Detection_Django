from django.shortcuts import render
from django.shortcuts import render
import pyrebase
from datetime import datetime as d
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

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
    if request.method == "POST":
        data = json.loads(request.body)
        lattitude = data.get("lattitude")
        longitude = data.get("longitude")
        accuracy = data.get("accuracy")
        print(lattitude)
        print(longitude)
        print(accuracy)
        # Do something with the variable data
        return HttpResponse(status=200)

    # if request.method == "POST":
    #     lattitude = request.POST.get('lattitude')
    #     longitude = request.POST.get('longitude')
    #     accuracy = request.POST.get('accuracy')
    #     print(lattitude)
    #     print(longitude)
    #     print(accuracy)
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
        date = json.dumps(d.now(), cls=DjangoJSONEncoder)
        print(full_name, complain_type, complain_description, phone, date)

        # Initialize Firebase app with credentials
        cred = credentials.Certificate(
            'static\css\json\serviceAccountKey.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://realtime-crime-detection-773bc-default-rtdb.firebaseio.com'
        })

        # Get a reference to the database service
        ref = db.reference()

        # Define the data to be inserted
        data = {
            'full_name': full_name,
            'complain_type': complain_type,
            'complain_description': complain_description,
            'phone': phone,
            'date': date
        }

        # Push the data to the database
        new_data_ref = ref.child('Crime_reports').push(data)

        # Print the newly generated unique key for the data
        print(new_data_ref.key)

        # Return a response
        return render(request, 'index.html')
    else:
        # Render the form
        return render(request, 'RegisterComplain.html')

    return render(request, 'RegisterComplain.html')
