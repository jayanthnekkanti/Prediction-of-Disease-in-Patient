from django.shortcuts import render

# Create your views here.

def register(request):
    if(request.method=="POST"):
        data= request.POST #store all the values of all the textboxes
        firstname = data.get('textfirstname')
        middlename = data.get('textmiddlename')#by the name of the textbox
        lastname = data.get('textlastname')
        if('buttonsubmit' in request.POST):
            result= firstname + middlename + lastname
            return render(request,'register.html',context={'result':result})
    return render(request,'register.html')

def employee(request):
    if(request.method=="POST"):
        data = request.POST
        emailid = data.get('textemailid')
        mobileno = data.get('textmobileno')
        if('buttonsubmit' in request.POST):
            result= emailid + mobileno
            return render(request,'employee.html',context={'result':result})
    return render(request,'employee.html')

def calci(request):
    if(request.method=="POST"):
        data = request.POST
        firstnumber = data.get('textfirstnumber')
        secondnumber = data.get('textsecondnumber')
        if('buttonadd' in request.POST):
            result = int(firstnumber) + int(secondnumber)
            return render(request,'calci.html',context={'result':result})
        if('buttonsub' in request.POST):
            result = int(firstnumber) - int(secondnumber)
            return render(request,'calci.html',context={'result':result})
        if('buttonmul' in request.POST):
            result = int(firstnumber) * int(secondnumber)
            return render(request,'calci.html',context={'result':result})
        if('buttondiv' in request.POST):
            result = int(firstnumber) / int(secondnumber)
            return render(request,'calci.html',context={'result':result})
    return render(request,'calci.html')

def index(request):
    return render(request,'index.html')

def marks(request):
    if(request.method=="POST"):
        data = request.POST
        hours=data.get('textmarks')
        age=data.get('textage')
        internet=data.get('textinternet')
        if('buttonpredict' in request.POST):
            import pandas as pd
            path="/Users/jayanthnekkanti/Desktop/day2/Data/Exammarks.csv"
            data=pd.read_csv(path)
            #print(data)
            medianvalue=data.hours.median()
            #print(medianvalue)

            data.hours=data.hours.fillna(medianvalue)
            #print(medianvalue)
            inputs=data.drop('marks',axis=1)
            #print(inputs)
            output=data.drop(['hours','age','internet'],axis=1)
            #print(output)
            import sklearn
            import math
            from sklearn import linear_model
            model=linear_model.LinearRegression()
            model.fit(inputs,output)
            result=model.predict([[float(hours),int(age),int(internet),]])
            return render(request,'marks.html',context={'result':result})
    return render(request,'marks.html')


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from django.shortcuts import render



def about(request):
    data = pd.read_csv('//Users//jayanthnekkanti//Desktop//GUI//basics//data.csv')
    data['SEX'] = data['SEX'].map({'F': 1, 'M': 0})
    data['SOURCE'] = data['SOURCE'].map({'in': 1, 'out': 0})
    inputs = data.drop('SOURCE', axis=1)
    output = data['SOURCE']

    x_train, x_test, y_train, y_test = train_test_split(inputs, output, test_size=0.2)

    model = RandomForestClassifier(n_estimators=50)
    model.fit(x_train, y_train)

    if request.method == 'POST':
        try:
            HAEMATOCRIT = float(request.POST.get('HAEMATOCRIT', 0))
            HAEMOGLOBINS = float(request.POST.get('HAEMOGLOBINS', 0))
            ERYTHROCYTE = float(request.POST.get('ERYTHROCYTE', 0))
            LEUCOCYTE = float(request.POST.get('LEUCOCYTE', 0))
            THROMBOCYTE = float(request.POST.get('THROMBOCYTE', 0))
            MCH = float(request.POST.get('MCH', 0))
            MCHC = float(request.POST.get('MCHC', 0))
            MCV = float(request.POST.get('MCV', 0))
            AGE = float(request.POST.get('AGE', 0))
            SEX = int(request.POST.get('SEX', 0))  # Assuming binary (0 or 1)
            

            result = model.predict([[HAEMATOCRIT, HAEMOGLOBINS, ERYTHROCYTE, LEUCOCYTE, THROMBOCYTE, MCH, MCHC, MCV, AGE, SEX]])

            if result[0] == 1:
                result_text = "Incare patient"
            else:
                result_text = "Outcare patient "

            if 'submitbutton' in request.POST:
                return render(request, 'about.html', {'result_text': result_text})
        except ValueError as ve:
            error_message = f"Invalid input: {ve}"
            return render(request, 'about.html', {'error_message': error_message})

    # Render the form if it's a GET request or if the form is not submitted
    return render(request, 'about.html')
5