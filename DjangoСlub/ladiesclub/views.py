from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives


from ladiesclub.message import get_message
from ladiesclub.models import News


def show_main_page(request):
    context = {
        'news': News.objects.all()
    }

    return render(request, 'index.html', context)


def send_message(fio, num, user_email, questions):
    #Текст сообщения
    email_text = get_message()
    email_text = email_text.replace('FIO', fio)
    email_text = email_text.replace('NUMBER', num)
    email_text = email_text.replace('EMAIL', user_email)
    email_text = email_text.replace('QUESTIONS', questions)

    message = EmailMultiAlternatives(
        'Заявка на членство',
        email_text,
        'awesome.ladys@yandex.ru',
        ['saint.4.script@gmail.com', 'lidiyapavlova@icloud.com']
    )
    message.attach_alternative(email_text, "text/html")
    message.send(fail_silently=False)


def send_form(request):
    data = request.POST
    fio = data.get('fio')
    num = data.get('phone_number')
    email = data.get('email')
    questions = data.get('questions')

    try:
        send_message(fio, num, email, questions)
        return JsonResponse(
            {
                'status': 'OK'
            }
        )
    except:
        return JsonResponse(
                {
                    'status': 'BAD'
                }
            )
