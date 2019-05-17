from django.shortcuts import render, redirect
from profile.models import Profile, SearchHistory
from profile.forms.profile_form import ProfileForm


def profile(request):
    profile = Profile.objects.filter( user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm( instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save( commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'profile/profile_index.html', {
        'form': ProfileForm(instance=profile),
        'profile': profile
    })


def searchHistory(request):
    history = SearchHistory.objects.filter(user=request.user)
    return render(request, 'profile/search_history.html', {"history": history})