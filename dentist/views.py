from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # data = {
        #     'message_name': message_name, 
        #     'message_email': message_email, 
        #     'message': message, 
        # }

        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # From email
            ['villandixon@yahoo.com'], # To email
        )

        # add try catch
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})        

def service(request):
    return render(request, 'service.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def appointment(request):
    if request.method == 'POST':
        name = request.POST['your-name']
        phone = request.POST['your-phone']
        email = request.POST['your-email']
        address = request.POST['your-address']
        schedule = request.POST['your-schedule']
        time = request.POST['your-time']
        message = request.POST['your-message']

        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'schedule': schedule,
            'time': time,
            'message': message
        }
        # send_mail(
        #     name +'-'+ phone, # subject
        #     message +'-'+ address  +'-'+ schedule  +'-'+ time, # message
        #     email, # From email
        #     ['villandixon@yahoo.com'], # To email
        # )

        # add try catch
        return render(request, 'appointment.html', data)
    else:
        return render(request, 'home.html', {})