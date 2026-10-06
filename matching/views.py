from django.shortcuts import render, redirect, get_object_or_404
from .models import RoommateProfile
from .forms import RoommateProfileForm
from .matching_engine import score_profile, explain, score_label

def current_profile():
    return RoommateProfile.objects.first()

def home(request):
    p = current_profile()
    total = RoommateProfile.objects.count()
    top_match = None
    average_score = None
    if p:
        scores = []
        for other in RoommateProfile.objects.exclude(pk=p.pk):
            score, _ = score_profile(p, other)
            scores.append((score, other))
        scores.sort(key=lambda x: x[0], reverse=True)
        if scores:
            top_match = {'profile': scores[0][1], 'score': scores[0][0], 'label': score_label(scores[0][0])[0]}
            average_score = round(sum(x[0] for x in scores) / len(scores))
    return render(request, 'matching/home.html', {
        'profile': p, 'profile_count': total, 'top_match': top_match,
        'average_score': average_score, 'factor_count': 10,
    })

def profile_form(request):
    p=current_profile()
    if request.method == 'POST':
        form=RoommateProfileForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('matches')
    else:
        form=RoommateProfileForm(instance=p)
    return render(request,'matching/profile_form.html',{'form':form,'editing':bool(p)})

def matches(request):
    p=current_profile()
    results=[]
    if p:
        for other in RoommateProfile.objects.exclude(pk=p.pk):
            score, details=score_profile(p,other)
            strong,weak=explain(details)
            results.append({'profile':other,'score':score,'details':details,'strong':strong,'weak':weak})
        results.sort(key=lambda x:x['score'],reverse=True)
    min_score = request.GET.get('min_score', '0')
    try:
        min_score = max(0, min(100, int(min_score)))
    except ValueError:
        min_score = 0
    filtered_results = [r for r in results if r['score'] >= min_score]
    return render(request,'matching/matches.html',{'profile':p,'results':filtered_results,'all_results':results,'min_score':min_score})

def match_detail(request,profile_id):
    p=current_profile(); other=get_object_or_404(RoommateProfile,pk=profile_id)
    score,details=score_profile(p,other)
    strong,weak=explain(details)
    label,label_class=score_label(score)
    return render(request,'matching/match_detail.html',{'profile':p,'other':other,'score':score,'details':details,'strong':strong,'weak':weak,'label':label,'label_class':label_class})

def profiles(request):
    return render(request,'matching/profiles.html',{'profiles':RoommateProfile.objects.all()})
