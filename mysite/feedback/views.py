from django.shortcuts import redirect
from .forms import FeedBackForm
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from mysite import settings

class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()

            name = request.POST['name']
            phone = request.POST['phone']
            description = request.POST['description']

            mailgroup = "{0} оставил заявку на посещение музея:\n\nТелефон оставившего заявку: {1}\n\nЖелаемые дата и время посещения: {2}".format(name, phone, description)
            send_mail('Новая запись на сайте "Дом Вверх Дном',
                      mailgroup,
                      settings.EMAIL_HOST_USER,
                      ['llcmadman@gmail.com'],
                      fail_silently=False)

            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, settings.MY_INFO, 'Заполнены не все поля!')
        return redirect("/")







