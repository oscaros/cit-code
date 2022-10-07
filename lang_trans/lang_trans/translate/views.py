from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from translate.helpers import load_languages
from .models import LanguagesModel, VotesModel
import socket

# Create your views here.
def homePage(request=None):     
    if request is not None:
        languages =LanguagesModel.objects.all().order_by('name')
        return render(request, "./translate.html", {'languages': languages})

def howItWorksPage(request=None):      
    return render(request, "./how_it_works.html")


def translateText(request):
    if request.method == 'GET': 
        TextToTranslate = request.GET['TextToTranslate']
        LanguageToTransTo = request.GET['LanguageToTransTo']
        translator = googletrans.Translator()
        data =translator.translate(TextToTranslate, dest = LanguageToTransTo).text

        return HttpResponse(data) # Sending data back to page
    else:
        return HttpResponse("Unknown request")

def autoDetectText(request):
    if request.method == 'GET':
        TextToTranslate = request.GET['TextToTranslate']

        #instantiate the trans object
        translator = googletrans.Translator()
        #data =translator.translate(TextToTranslate, dest = LanguageToTransTo).text
        data = translator.detect(TextToTranslate) #detect(lang=en, ,confidence=None)
        return HttpResponse(data)

    else:
        return HttpResponse("Unknown request")

def SaveRating(request):
    if request.method == 'GET':
        rating = request.GET['rating']   
        hostname=socket.gethostname()   
        ip=socket.gethostbyname(hostname) 
       
        rating_model = VotesModel()
        rating_model.ip = ip
        rating_model.rating =  rating
        rating_model.save()




# def SpeechToText(request):
#     if request.method == 'GET':

