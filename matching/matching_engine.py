WEIGHTS = {
    'budget': 15, 'sleep': 15, 'cleanliness': 15, 'food': 10, 'smoking': 15,
    'social': 10, 'noise': 10, 'guests': 5, 'cooking': 5, 'study_work': 5,
}
LABELS = {
    'budget':'Budget', 'sleep':'Sleep schedule', 'cleanliness':'Cleanliness', 'food':'Food preference',
    'smoking':'Smoking', 'social':'Social style', 'noise':'Noise tolerance', 'guests':'Guests',
    'cooking':'Cooking', 'study_work':'Study/work routine'
}

ORDER = {'sleep': {'early':0,'normal':1,'late':2}, 'cleanliness': {'low':0,'medium':1,'high':2},
         'social': {'quiet':0,'balanced':1,'social':2}, 'noise': {'quiet':0,'moderate':1,'loud':2},
         'guests': {'rare':0,'sometimes':1,'often':2}}

def closeness(a, b, field):
    if field == 'budget':
        diff = abs(a.budget - b.budget)
        return max(0, 1 - diff / max(a.budget, b.budget, 1))
    if field in ('cooking','study_work'):
        return 1.0 if getattr(a, field) == getattr(b, field) else 0.35
    if field == 'food':
        if a.food == b.food: return 1.0
        if 'both' in (a.food, b.food): return 0.8
        return 0.2
    if field == 'smoking':
        if a.smoking == b.smoking: return 1.0
        if 'never' in (a.smoking, b.smoking): return 0.0
        return 0.5
    av, bv = getattr(a, field), getattr(b, field)
    if av == bv: return 1.0
    ranks = ORDER[field]
    return max(0, 1 - abs(ranks[av]-ranks[bv])/2)

def score_profile(a, b):
    details=[]
    total=0
    for field, weight in WEIGHTS.items():
        similarity=closeness(a,b,field)
        earned=round(similarity*weight, 1)
        total += earned
        details.append({'field':field,'label':LABELS[field],'weight':weight,'similarity':similarity,'earned':earned})
    return round(total), details

def explain(details):
    strong=sorted(details,key=lambda x:x['similarity'],reverse=True)[:3]
    weak=sorted(details,key=lambda x:x['similarity'])[:3]
    return strong, weak


def score_label(score):
    if score >= 85:
        return 'Excellent match', 'excellent'
    if score >= 70:
        return 'Good match', 'good'
    if score >= 55:
        return 'Fair match', 'fair'
    return 'Low match', 'low'
