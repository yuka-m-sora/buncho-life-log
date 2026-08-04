from django.shortcuts import render, get_object_or_404, redirect
from .models import Bird, WeightRecord, BehaviorRecord
from .forms import WeightRecordForm, BehaviorRecordForm
from django.db.models import Avg, Max, Min, Count


def home(request):
    birds = Bird.objects.all()
    return render(request, 'birds/home.html', {'birds': birds})

def bird_detail(request, bird_id):
    bird = get_object_or_404(Bird, id=bird_id)

    # 体重履歴表示用は新しい順
    weights = WeightRecord.objects.filter(bird=bird).order_by('-date')
    # 行動記録は新しい順に表示
    behaviors = BehaviorRecord.objects.filter(
        bird=bird
    ).order_by('-date', '-id')
    # グラフ表示用は日付昇順で取得
    graph_weights = WeightRecord.objects.filter(bird=bird).order_by('date')

    latest_weight = weights.first()
    average_weight = weights.aggregate(Avg('weight'))['weight__avg']
    max_weight = weights.aggregate(Max('weight'))['weight__max']
    min_weight = weights.aggregate(Min('weight'))['weight__min']
    record_count = weights.count()

    graph_labels = [record.date.strftime('%Y-%m-%d') for record in graph_weights]
    graph_data = [float(record.weight) for record in graph_weights]

    return render(request, 'birds/bird_detail.html', {
        'bird': bird,
        'weights': weights,
        'behaviors': behaviors,
        'latest_weight': latest_weight,
        'average_weight': average_weight,
        'max_weight': max_weight,
        'min_weight': min_weight,
        'record_count': record_count,
        'graph_labels': graph_labels,
        'graph_data': graph_data,
    })

def add_weight(request, bird_id):
    bird = get_object_or_404(Bird, id=bird_id)

    if request.method == 'POST':
        form = WeightRecordForm(request.POST)
        if form.is_valid():
            weight_record = form.save(commit=False)
            weight_record.bird = bird
            weight_record.save()
            return redirect('bird_detail', bird_id=bird.id)
    else:
        form = WeightRecordForm()

    return render(request, 'birds/add_weight.html', {
        'bird': bird,
        'form': form,
    })

def edit_weight(request, weight_id):
    weight_record = get_object_or_404(WeightRecord, id=weight_id)
    bird = weight_record.bird

    if request.method == 'POST':
        form = WeightRecordForm(request.POST, instance=weight_record)
        if form.is_valid():
            form.save()
            return redirect('bird_detail', bird_id=bird.id)
    else:
        form = WeightRecordForm(instance=weight_record)

    return render(request, 'birds/edit_weight.html', {
        'bird': bird,
        'form': form,
        'weight_record': weight_record,
    })

def delete_weight(request, weight_id):
    weight_record = get_object_or_404(WeightRecord, id=weight_id)
    bird = weight_record.bird

    if request.method == 'POST':
        weight_record.delete()
        return redirect('bird_detail', bird_id=bird.id)

    return render(request, 'birds/delete_weight.html', {
        'bird': bird,
        'weight_record': weight_record,
    })

def add_behavior(request, bird_id):
    bird = get_object_or_404(Bird, id=bird_id)

    if request.method == 'POST':
        form = BehaviorRecordForm(request.POST)

        if form.is_valid():
            behavior = form.save(commit=False)
            behavior.bird = bird
            behavior.save()

            return redirect(
                'bird_detail',
                bird_id=bird.id
            )
        else:
            print(form.errors)

    else:
        form = BehaviorRecordForm()

    return render(
        request,
        'birds/add_behavior.html',
        {
            'bird': bird,
            'form': form,
        }
    )

