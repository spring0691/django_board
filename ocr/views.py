from django.shortcuts import render
import pytesseract
from PIL import Image


# Create your views here.
def index(request):
    context = {}
    
    if request.method == "POST":
        pic = request.FILES.get('pic')           # 번역할 기사파일을 받아옴
        nat = request.POST.get('nat')            # 언어 설정값 받아옴
        pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
        img = Image.open(pic)                    # 그걸 이미지로 열고

        text = pytesseract.image_to_string(img, lang=nat)    # 프로그램 깐거 돌리는 명령어 이용해서 이미지 + 언어 설정해서 나온결과를 text에 저장
        
        context.update({                     
            'con'    : text,                      
            'nat'    : nat        
        })

    
    return render(request,'ocr/index.html',context) # news에 저장된 값을 다시 리턴해서 index.html로 보냄

