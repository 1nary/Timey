from django.shortcuts import render
from create.models import Lecture
from django.shortcuts import redirect
from create.forms import createForm
    
def index(request):
  data = Lecture.objects.all().order_by('week','period')
  if(request.method == 'POST'):
    obj = Lecture()
    week = request.POST['week']
    period = request.POST['period']
    if Lecture.objects.filter(week=week,period=period).exists():
      print('')
    else:
      LectureInfo = createForm(request.POST, instance=obj)
      LectureInfo.save()
    return redirect(to='/')
  params = {
    'form': createForm(),
    'data': data,
    'title': '履修作成',
  }
  return render(request, 'create/index.html', params)

def edit(request,num):
  data = Lecture.objects.all()
  obj = Lecture.objects.get(id=num)
  params = {
    'data': data,
    'form': createForm(instance=obj),
    'title': '履修更新',
  }
  if(request.method == 'POST'):
    LectureInfo = createForm(request.POST, instance=obj)
    LectureInfo.save()
    return redirect(to='/')
  return render(request, 'create/edit.html', params)

def delete(request, num):
  data = Lecture.objects.all()
  lecture = Lecture.objects.get(id=num)
  if(request.method=='POST'):
    lecture.delete()
    return redirect(to='/')
  params = {
    'data': data,
    'id': num,
    'obj': lecture,
    'title': '履修削除',
  }
  return render(request, 'create/delete.html',params)
