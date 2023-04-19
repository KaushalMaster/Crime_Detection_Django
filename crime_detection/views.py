from django.shortcuts import render
import pyrebase
# Create your views here.
config = {
    apiKey: "AIzaSyAcv7rjtb0TPvaMoRdeqSlUUpiyjjNbioY",
    authDomain: "realtime-crime-detection-773bc.firebaseapp.com",
    projectId: "realtime-crime-detection-773bc",
    storageBucket: "realtime-crime-detection-773bc.appspot.com",
    messagingSenderId: "446675461946",
    appId: "1:446675461946:web:c2b9e2b657e0932e3dd203"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def index(request):
    data = database.child('')
    return render(request, 'index.html')
