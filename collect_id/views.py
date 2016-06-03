from django.shortcuts import render, redirect
# Create your views here.
from .models import Info
from .forms import InfoForm, DeleteForm
def index(request):
    users = list(Info.objects.all())
    return render(request, 'index.html', {'users':users})

def add_info(request):
    if request.method == 'POST':
        try:
            ins = Info.objects.get(stu_id=request.POST['stu_id'])
            print(ins.name)
        except Exception as e:
            print(e)
            ins = Info()
        f = InfoForm(request.POST, instance=ins)
        f.save()
        return redirect('/')
    else:
        form = InfoForm()
        return render(request, 'add_info.html', {'form':form})

def delete_info(request):
    if request.method == 'POST':
        try:
            print(request.POST['stu_id'])
            ins = Info.objects.get(stu_id=request.POST['stu_id'])
            ins.delete()
            return redirect('/')
        except:
            return redirect('/')
    else:
        form = DeleteForm()
        return render(request, 'delete_info.html', {'form':form})