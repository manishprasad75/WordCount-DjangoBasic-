from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        text = request.POST.get('text')
        words = text.split()
        count = len(words)
        wordDict = dict()
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1;
        context = {
            'text' : text,
            'count' : count,
            'wordDict': wordDict
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')