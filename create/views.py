from django.shortcuts import render
from create.models import Lecture
from django.shortcuts import redirect
from create.forms import createForm
    
def index(request):
  data = Lecture.objects.all()
  if(request.method == 'POST'):
    obj = Lecture()
    week = request.POST['week']
    period = request.POST['period']
    if Lecture.objects.filter(week=week,period=period).exists():
      print('')
    else:
      LectureInfo = createForm(request.POST, instance=obj)
      LectureInfo.save()
    return redirect(to='/timetable')
  params = {
    'form': createForm(),
    'data': data,
    'title': '＃時間割作成',
  }
  return render(request, 'create/index.html', params)

def edit(request,num):
  data = Lecture.objects.all()
  obj = Lecture.objects.get(id=num)
  params = {
    'data': data,
    'form': createForm(instance=obj),
    'title': '＃時間割更新・削除',
  }
  if(request.method == 'POST'):
    LectureInfo = createForm(request.POST, instance=obj)
    LectureInfo.save()
    return redirect(to='/timetable')
  return render(request, 'create/edit.html', params)

def delete(request, num):
  data = Lecture.objects.all()
  lecture = Lecture.objects.get(id=num)
  if(request.method=='POST'):
    lecture.delete()
    return redirect(to='/timetable')
  params = {
    'data': data,
    'id': num,
    'obj': lecture,
    'title': '＃時間割更新・削除',
  }
  return render(request, 'create/delete.html',params)
