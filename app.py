import pyrebase
import firebase_admin,os
from firebase_admin import credentials
from pyfcm import FCMNotification

p = os.path.abspath(os.getcwd()) +"\\techcamp.json"
cred = credentials.Certificate(p)
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyDf5HAk1zwLMMUNJIfK2RN0N3NznxFTJ5g",
    "authDomain": "elearn-demo-af5b5.firebaseapp.com",
    "databaseURL": "https://elearn-demo-af5b5.firebaseio.com",
    "projectId": "elearn-demo-af5b5",
    "storageBucket": "elearn-demo-af5b5.appspot.com",
    "messagingSenderId": "736845008000",
    "appId": "1:736845008000:web:006266c7edfea5f8afaa65",
    "measurementId": "G-XZ8FLB0EQC"
}

firebase = pyrebase.initialize_app(firebaseConfig)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=p


push_service = FCMNotification(api_key="AIzaSyDf5HAk1zwLMMUNJIfK2RN0N3NznxFTJ5g")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "cJIrEDqjSVI:APA91bEbi6LRSqJ-3PH0fGviD-BLH9WbkXSdcIRNkPU4jxzSVujnL-00845r6lkRSKsKvFQz9NkfThzbBFaoaoD_ZmJVoH-FHqDk9f6oJwITT8SFODABKmLo2Zi9mUxc5rsLX_fyYyXS"
message_title = u"Mbuzi"
message_body = u"Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print(result)