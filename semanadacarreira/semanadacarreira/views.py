from django.shortcuts import render
from core.forms import formProf
from core.models import Pessoa

def view_aluno(request):
    lista = Pessoa.objects.all()
    return render(request, 'alunos.html', {"lista": lista})

def view_prof(request):
    form=formProf()
    if request.method == 'POST':
        form = formProf(request.POST)
        if form.is_valid():
            # print(form)
            form.save()
            return render(request, 'registrado.html')

    return render(request, 'index.html', {'form': form})
