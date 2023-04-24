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
from google.oauth2 import service_account
import google.auth.transport.requests
import requests

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

# Initialize Firebase app with credentials
cred = credentials.Certificate(
    'static\css\json\serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-crime-detection-773bc-default-rtdb.firebaseio.com'
})


def index(request):
    # if request.method == "POST":
    #     data = json.loads(request.body)
    #     lattitude = data.get("lattitude")
    #     longitude = data.get("longitude")
    #     accuracy = data.get("accuracy")
    #     print(lattitude)
    #     print(longitude)
    #     print(accuracy)
    #     # Do something with the variable data
    #     return HttpResponse(status=200)

    # if request.method == "POST":
    #     lattitude = request.POST.get('lattitude')
    #     longitude = request.POST.get('longitude')
    #     accuracy = request.POST.get('accuracy')
    #     print(lattitude)
    #     print(longitude)
    #     print(accuracy)

    # if request.method == 'POST':
    #     data = request.POST.get('data')
    #     print(data.lattitude)
    #     print(data.longitude)
    #     print(data.accuracy)
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


def myadmin(request):
    # complain_id = database.child('Crime_reports').child('id').get().val()
    # complain_description = database.child('Crime_reports').child(
    #     'complain_description').get().val()
    # complain_date = database.child('Crime_reports').child('data').get().val()
    # complain_by_name = database.child(
    #     'Crime_reports').child('full_name').get().val()
    # complain_by_phone = database.child(
    #     'Crime_reports').child('phone').get().val()

    # print(complain_id)
    # print(complain_description)
    # print(complain_date)
    # print(complain_by_name)
    # print(complain_by_phone)

    # data = {
    #     "complain_id": complain_id,
    #     "complain_description": complain_description,
    #     "complain_date": complain_date,
    #     "complain_by_name": complain_by_name,
    #     "complain_by_phone": complain_by_phone
    # }

    # cred = credentials.Certificate(
    #     'static\css\json\serviceAccountKey.json')
    # firebase_admin.initialize_app(cred, {
    #     'databaseURL': 'https://realtime-crime-detection-773bc-default-rtdb.firebaseio.com'
    # })

    ref = db.reference()

    # converting list to dictionary
    data = []
    snapshot = ref.child('Crime_reports').get()
    for key, val in snapshot.items():
        data.append(dict(val))

    # print(data[0])

    complain_description = data[0]['complain_description']
    complain_type = data[0]['complain_type']
    complain_date = data[0]['date']
    complain_by_name = data[0]['full_name']
    complain_by_phone = data[0]['phone']

    # last try
    # credentials = service_account.Credentials.from_service_account_file(
    #     "static\css\json\serviceAccountKey.json"
    # )

    # access_token_info = credentials.fetch_oauth2_token()
    # access_token = access_token_info["access_token"]

    # response = requests.get(
    #     "https://https://realtime-crime-detection-773bc-default-rtdb.firebaseio.com/static\css\json\serviceAccountKey.json?auth=" + access_token
    # )

    # print(complain_type)
    # complaints = data

    mydata = {
        'description': complain_description,
        'type': complain_type,
        'date': complain_date,
        'name': complain_by_name,
        'phone': complain_by_phone
    }

    print(mydata)
    return render(request, 'Admin.html', context={'mydata': mydata})
