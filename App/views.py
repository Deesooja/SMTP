from django.shortcuts import render
from rest_framework.views import APIView
from App.Response import endpointResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

class EmailSend(APIView):
    def get(self, request):
        from_email = settings.EMAIL_HOST_USER
        subject = "Testing"
        message = "This Email Send Using "
        recipient_list = ["prksvsvkrma@gmail.com"]
        return_value = send_mail(subject, message, from_email, recipient_list)
        print("return_value", return_value)
        render_to_string("email_template.html")
        return endpointResponse(status_code=200, massage="Ok", data=[])

class HtmlTemplateSendByEmail(APIView):
    def get(self, request):
        from_email = settings.EMAIL_HOST_USER
        subject = "Testing"
        recipient_list = ["prksvsvkrma@gmail.com"]
        contant = "This Email Send By Django and Code by Deesooja"

        html_contant = render_to_string("email_template.html", {'contant': contant})
        text_contant = strip_tags(html_contant)
        email = EmailMultiAlternatives(subject, text_contant, from_email, recipient_list)
        email.attach_alternative(html_contant, 'text/html')
        print(email.send())
        print("clicked")
        return endpointResponse(status_code=200, massage="Ok", data=[])

