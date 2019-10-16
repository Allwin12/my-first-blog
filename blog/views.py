from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
import wikiquote


def wallethome(request):
    return render(request,'blog/home.html');

def wallet(request):
    return render(request,'blog/wallet.html');

def importwallet(request):
    return render(request,'blog/import.html');

def post_list(request):
    str=wikiquote.quote_of_the_day()
    quote=str[0]
    author=str[1]
    context={'quote':quote,'author':author}
    return render(request, 'blog/post_list.html',context)

def contact(request):
    return render(request, 'blog/contact.html',{})

def resume(request):
    return render(request,'blog/resume.html',{})

def home(request):
    return render(request,'blog/post_list.html',{})

def feedback(request):
    if request.method == 'POST':
        receiving_mail = request.POST['sender']
        feedback = request.POST['comment']
        send_mail('New feedback','sender:'+receiving_mail+'\nfeedback:'+feedback, 'mailtoallwinraju@gmail.com', ['allwindicaprio@gmail.com'], fail_silently=False)
        send_mail('greetings', 'Hi, Thank you for subscribing!', 'mailtoallwinraju@gmail.com', [receiving_mail], fail_silently=False)
        return HttpResponse('Subscribed')
    else:
        return render(request,'blog/feedback.html')

def blog(request):
    return render(request,'blog/blog.html')
