from django.shortcuts import render, redirect
# Create your views here.
from .models import Info
from .forms import InfoForm, DeleteForm
from .get_rating import get_bc_rating, get_cf_rating
def index(request):
    users = list(reversed(Info.objects.order_by('score')))
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
        f.update_score()
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


def score_detail(request):
    stu_id = request.GET.get('stu_id')
    usr = Info.objects.get(stu_id=stu_id)
    return render(request, 'score_detail.html', {'usr':usr})

def update_all(request):
    users = Info.objects.all()
    for usr in users:
        usr.update_score()
    return redirect('/')

def update_score(request):
    stu_id = request.GET.get('stu_id')
    usr = Info.objects.get(stu_id=stu_id)
    print(usr.cf_id)
    usr.update_score()
    return redirect('../score_detail/?stu_id=' + stu_id)