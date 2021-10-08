from django.shortcuts import redirect, render
from acc.models import User
import os

from quiz.models import Quiz

# Create your views here.
def index(request):
    q = Quiz.objects.all()
    u = User.objects.all().order_by("-point")

    context = {
        'con' : q,
        'u' : u
    }
    return render(request,'quiz/index.html',context)

def 판단(답, 제출한답, 문제번호):
    if 문제번호 <=2:
        if 답 == 제출한답:
            return True
        f = open("test.py", "w")
        f.write(제출한답)
        f.close()

        if 답 == os.popen("python test.py").read().strip():
            return True

def judge(request, num):

    q = Quiz.objects.get(id=num)
    a = request.POST.get("answer")

    if 판단(q.answer,a,int(num)) == a:
        if not request.user in q.solver.all():
            q.solver.add(request.user)
            u = User.objects.get(username=request.user.username)
            u.point += q.point
            u.save()

    return redirect("quiz:index")
