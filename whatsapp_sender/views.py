from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from whatsapp_sender.whatsapp import WhatsApp


class SendMessage(View):
    whatsapp = WhatsApp()

    def get(self, request):
        return render(request, "whatsapp_sender/get_data.html", {"qr_code": self.whatsapp.get_qr_code()})

    def post(self, request):
        try:
            name = request.POST['name']
            message = request.POST['message']
        except:
            return render(request, "whatsapp_sender/get_data.html", {"message": 'Invalid Data'})
        else:
            try:
                self.whatsapp.send_message(name, message)
            except Exception as e:
                return HttpResponse(str(e))
            else:
                return HttpResponse('Success')
