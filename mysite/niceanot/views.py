from django.contrib import messages
from django.shortcuts import render

from niceanot import markov_api


# Create your views here.
def index(request):
    num_of_sentences = 1
    generated = ""

    try:
        if request.method == 'POST':
            print(request.POST)
            num_of_sentences = int(request.POST['num_of_sentences'])

            generated = markov_api.generate_sentences(num=num_of_sentences)

    except Exception as e:
        messages.error(request, str(e))

    context = {'num_of_sentences': num_of_sentences, 'result': generated}
    return render(request, 'niceanot/index.html', context)
