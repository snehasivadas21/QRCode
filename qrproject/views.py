from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            url=form.cleaned_data['url']

            qr = qrcode.make(url)
            file_name=name.replace(" ","").lower()+'.png'
            file_path=os.path.join(settings.MEDIA_ROOT , file_name)
            qr.save(file_path)

            qr_url = os.path.join(settings.MEDIA_URL,file_name)

            context={'name':name,'qr_url':qr_url,'file_name':file_name}
            return render(request,'qr_result.html',context)
            
    else:
        form=QRCodeForm()
        context={'form':form}
        return render(request,'generate_qr.html',context)