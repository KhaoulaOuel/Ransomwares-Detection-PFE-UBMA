import pickle
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ModelFile, Resultat


def home(request):
    return render(request, 'users/home.html')




def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully !')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})




@login_required()

def start(request):
    print("Hi")

    return render(request, 'users/start.html')



def result(request):
    Result = ""
    File = request.FILES['file'] 

    data = pd.read_csv(File , index_col=False, sep=';') 
    Algo = request.POST['Algo']


    if 'Random Forest' in request.POST['Algo'] and request.FILES: 

      loaded_model = pickle.load(open('rf.sav', 'rb')) 
      result = loaded_model.predict(data) 


      if result == 0:
         Result = "Not ransomware"
         print("not ransomware")

      elif result == 1:
         Result = "Ransomware"
         print ("ransomware")

      else:
         Result = "error"
         print ("error")
      file = ModelFile.objects.create(filename=File)
      rslt = Resultat.objects.create(filename=file,result=Result,model_name='Random Forest')

      file.save()
      rslt.save()

    if 'Support Vector Machine' in request.POST['Algo']:
     
      loaded_model = pickle.load(open('svm.sav', 'rb'))
      result = loaded_model.predict(data)

      if result == 0:
         Result = "Not ransomware"
         print("not ransomware")

      elif result == 1:
         Result = "Ransomware"
         print ("ransomware")

      else:
         Result = "error"
         print ("error")

      file = ModelFile.objects.create(filename=File)
      rslt = Resultat.objects.create(filename=file, result=Result, model_name='Support Vector Machine')

      file.save()
      rslt.save()

    if 'Multi-Layer Perceptron' in request.POST['Algo']:
    
     loaded_model = pickle.load(open('mlp.sav', 'rb'))
     result = loaded_model.predict(data)

     if result == 0:
         Result = "Not ransomware"
         print("not ransomware")

     elif result == 1:
         Result = "Ransomware"
         print ("ransomware")

     else:
         Result = "error"
         print ("error")
     file = ModelFile.objects.create(filename=File)
     rslt = Resultat.objects.create(filename=file, result=Result, model_name='Multi-Layer Perceptron')

     file.save()
     rslt.save()

    if 'Decision Tree' in request.POST['Algo']:

    
     loaded_model = pickle.load(open('dtc.sav', 'rb'))
     result = loaded_model.predict(data)

     if result == 0:
         Result = "Not ransomware"
         print("not ransomware")

     elif result == 1:
         Result = "Ransomware"
         print ("ransomware")

     else:
         Result = "error"
         print ("error")

     file = ModelFile.objects.create(filename=File)
     rslt = Resultat.objects.create(filename=file, result=Result, model_name='Decision Tree')

     file.save()
     rslt.save()
    if 'Logistic Regression' in request.POST['Algo']:
    
     loaded_model = pickle.load(open('clfr.sav', 'rb'))
     result = loaded_model.predict(data)

     if result == 0:
         Result = "Not ransomware"
         print("not ransomware")

     elif result == 1:
         Result = "Ransomware"
         print ("ransomware")

     else:
         Result = "error"
         print ("error")

     file = ModelFile.objects.create(filename=File)
     rslt = Resultat.objects.create(filename=file, result=Result, model_name='Logistic Regression')

     file.save()
     rslt.save()
    if 'AdaBoost with Decision Tree' in request.POST['Algo']:
    
     loaded_model = pickle.load(open('AdaBoostDT.sav', 'rb'))
     result = loaded_model.predict(data)


     if result == 0:
         Result = "Not ransomware"
         print("not ransomware")

     elif result == 1:
         Result = "Ransomware"
         print ("Ransomware")

     else:
         Result = "error"
         print ("error")

     file = ModelFile.objects.create(filename=File)
     rslt = Resultat.objects.create(filename=file, result=Result, model_name='AdaBoost with Decision Tree')

     file.save()
     rslt.save()




    context = { 'File' : File, 'Algo' : Algo, 'Result' : Result }
    


    return render(request, 'users/result.html',context) 
    

    
    



    
