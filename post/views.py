from django.shortcuts import render, HttpResponse, render

# Create your views here.
def home(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        if num == "1":
            print("===> Test home function")
        else:
            raise ValueError("A test error occurred!")

    return render(request, 'post/home.html')