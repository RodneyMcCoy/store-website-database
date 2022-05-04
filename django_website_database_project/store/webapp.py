from django.shortcuts import render

def button(request):

    return render(request,'geniusvoice.html')

def output(request):
    
    output_data = "This is a string. Idk"
    
    return render(request,"geniusvoice.html", {"output_data":output_data})
    