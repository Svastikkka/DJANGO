from django.shortcuts import render
from signup.forms import NewFormUser


# Create your views here.
def index(request):
    return render(request, 'help/help.html')


def signup(request):
    form = NewFormUser()
    if request.method == 'POST':
        form = NewFormUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request) # need to fix
        else:
            print("FORM INVALID")
    return render(request, "signup/signup.html", {'form': form})
