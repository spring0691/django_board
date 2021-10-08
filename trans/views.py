from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        text = request.POST.get('before')
        print(1)
        print(text)
        if text:
            print(2)
            f = request.POST.get('from')
            t = request.POST.get('to')

            translator = Translator()
            if not f or not t:
                print(3)
                trans = translator.translate(text, dest="ko")
            else:
                print(4)
                trans = translator.translate(text, src=f, dest=t)
            context.update({
                'before' : text,
                'after' : trans.text,
                'from' : f,
                'to': t
            })
        

    return render(request, "trans/index.html", context)



    

