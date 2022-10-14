from django.shortcuts import render

# Create your views here.

def babtrahome(request):
    return render(request,'baabtrasit/baabtra.html')


def page1(request):
    return render(request,'baabtrasit/page.html')


def aboutus(request):
    return render(request,'baabtrasit/aboutus.html')


def files1(request):
    return render(request,'baabtrasit/file.html')


def files2(request):
    return render(request,'baabtrasit/files2.html') 


def grid1(request):
    return render(request,'baabtrasit/nwepage.html') 


def flex(request):
    return render(request,'baabtrasit/gridflex.html') 


def pgn(request):
    return render(request,'baabtrasit/pagenew.html')  


def ned(request):
    return render(request,'baabtrasit/newdiv.html')   
    
     
def baab(request):
    return render(request,'baabtrasit/btapage.html')  


def btsp(request):
    return render(request,'baabtrasit/bootstp.html')

