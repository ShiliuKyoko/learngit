from django.db import models
from mongoengine import *
from mongoengine import connect
connect('Pig', host='127.0.0.1', port=27017)
# Create your models here.

class Blong(Document):
    tittle = StringField()
    sex = StringField()
    price = StringField()
    address = StringField()
    lanlord_name = StringField()
    landlord_url = StringField()
    detail_url = StringField()

    meta = {'collection':'second_info'}

# for i in Blong.objects[:1]:
#     print(i.tittle)



