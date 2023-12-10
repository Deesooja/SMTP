from  django.urls import path
from App.views import EmailSend, HtmlTemplateSendByEmail



urlpatterns = [
path("mail", EmailSend.as_view(), name="text_mail"),
path("mail/html-template", HtmlTemplateSendByEmail.as_view(), name="Html_template_mail")
]


# my_dict = {
#     "emails":["Dee@gmail.com", "Dee@gmail.com", "Dee@gmail.com",]
# }