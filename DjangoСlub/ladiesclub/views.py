import smtplib as smtp
from getpass import getpass
from email.mime.text import MIMEText
from email.header import Header

from django.shortcuts import render
from django.http import JsonResponse
from django.template.context_processors import csrf

from ladiesclub.message import get_message
from ladiesclub.models import News


def show_main_page(request):
    info = {}
    info.update(csrf(request))

    news = News.objects.all()
    info['news'] = news

    return render(request, 'index.html', info)


def send_message(fio, num, user_email, questions):
    # Почта с которой отправляем
    email = 'awesome.ladys@yandex.ru' 
    # Пароль от нее
    password = 'bpbgfhjkm' 
    # Тема письма                   
    subject = 'Заявка на членство' 
    # Почта на которую отправляем
    dest_email = 'saint.4.script@gmail.com'

    #Текст сообщения
    email_text = get_message()

    email_text = email_text.replace('FIO', fio)
    email_text = email_text.replace('NUMBER', num)
    email_text = email_text.replace('EMAIL', user_email)
    email_text = email_text.replace('QUESTIONS', questions)
    
    #Это для нормальной отправки русского текста (на маке по крайней мере по-другому никак:( )
    msg = MIMEText( email_text, 'html', 'utf-8') 
    msg['Subject'] = Header( subject, 'utf-8')
    msg['From'] = email
    msg['To'] = dest_email  

    check = True
    server = smtp.SMTP_SSL('smtp.yandex.com.tr', 465)
    server.set_debuglevel(1)
    try:
        server.ehlo(email)
        server.login(email, password)
        server.auth_plain()
        server.sendmail(msg['From'], dest_email, msg.as_string())
    except:
        check = False
    finally:
        server.quit()
        return check


def send_form(request):
    data = request.POST
    fio = data.get('fio')
    num = data.get('phone_number')
    email = data.get('email')
    questions = data.get('questions')

    checker = send_message(fio, num, email, questions)

    if checker:
        return JsonResponse(
            {
                "status": "Ok"
            }
        )
    else:
        return JsonResponse(
            {
                'status': 'Fail'
            }
        )
