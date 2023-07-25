from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Photo
import random



def index(request):
    source = list(Photo.objects.values('img'))
    lengthsource= len(source)
    store=[]
    image1=[]
    image2 = []
    while True:
        source = list(Photo.objects.values('img'))
        lenght = len(source)
        ran = []
        ran2 = []
        for i in range(0, int(lenght / 2)):
            rand = random.choice(source)
            rand2 = random.choice(source)
            if rand in ran:
                print("contasdfsadfsadfsaiudhfisadhfuashfinue")
                break
            elif rand2 in ran:
                print("is it klsdfjsadfkljads")
                break
            ran.append(rand)
            ran2.append(rand2)
            data1,data2 = str(rand) ,str(rand2)
            data1,data2 = data1[9:-2],data2[9:-2]
            return render(request, "image/index.html", {"img1": data1, "img2": data2})
            print(len(ran))
            print(len(ran2))















    # dic = {'img1':image1,"img2":image2}
    return render(request, "image/index.html")


