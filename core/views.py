from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Medico, Consulta

def agendar(request):
    if request.method == 'POST':
        # 1. Pegar os dados que o usuário preencheu no formulário
        medico_id = request.POST.get('medico_id')
        paciente_nome = request.POST.get('paciente_nome')
        data = request.POST.get('data')
        motivo = request.POST.get('motivo')

        # 2. Salvar no Banco de Dados
        medico_escolhido = Medico.objects.get(id=medico_id)
        
        Consulta.objects.create(
            medico=medico_escolhido,
            paciente_nome=paciente_nome,
            data_consulta=data,
            motivo=motivo
        )
        
        # 3. Mostrar mensagem de sucesso
        messages.success(request, 'Consulta agendada com sucesso!')
        return redirect('agendar')

    # Se for apenas carregar a página (GET), busca os médicos para mostrar na lista
    medicos = Medico.objects.all()
    return render(request, 'agendar.html', {'medicos': medicos})