from data.models import Letter
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'home.html')

def upload(request):
    return render(request, 'upload.html')


def get_context():
    mittente_list = Letter.objects.values_list('mittente', flat=True).distinct()
    destinatario_list = Letter.objects.values_list('destinatario', flat=True).distinct()
    luogo_di_spedizione_list = Letter.objects.values_list('luogo_di_spedizione', flat=True).distinct()
    luogo_di_conservazione_list = Letter.objects.values_list('luogo_di_conservazione', flat=True).distinct()
    fondo_list = Letter.objects.values_list('fondo', flat=True).distinct()
    numerazione_list = Letter.objects.values_list('numerazione', flat=True).distinct()
    numero_prima_carta_list = Letter.objects.values_list('numero_prima_carta', flat=True).distinct()
    Facciata_prima_carta_list = Letter.objects.values_list('Facciata_prima_carta', flat=True).distinct()
    numero_totale_facciate_list = Letter.objects.values_list('numero_totale_facciate', flat=True).distinct()
    tipologia_lettera_list = Letter.objects.values_list('tipologia_lettera', flat=True).distinct()
    presenza_nota_di_ricezione_list = Letter.objects.values_list('presenza_nota_di_ricezione', flat=True).distinct()
    presenza_indirizzo_list = Letter.objects.values_list('presenza_indirizzo', flat=True).distinct()
    presenza_filigrana_list = Letter.objects.values_list('presenza_filigrana', flat=True).distinct()
    presenza_sigillo_list = Letter.objects.values_list('presenza_sigillo', flat=True).distinct()
    presenza_firma_list = Letter.objects.values_list('presenza_firma', flat=True).distinct()
    altezza_list = Letter.objects.values_list('altezza', flat=True).distinct()
    trascrittore_list = Letter.objects.values_list('trascrittore', flat=True).distinct()
    larghezza_list = Letter.objects.values_list('larghezza', flat=True).distinct()

    context = {
        'mittente_list': mittente_list,
        'destinatario_list': destinatario_list,
        'luogo_di_spedizione_list': luogo_di_spedizione_list,
        'luogo_di_conservazione_list': luogo_di_conservazione_list,
        'fondo_list': fondo_list,
        'numerazione_list': numerazione_list,
        'numero_prima_carta_list': numero_prima_carta_list,
        'Facciata_prima_carta_list': Facciata_prima_carta_list,
        'numero_totale_facciate_list': numero_totale_facciate_list,
        'tipologia_lettera_list': tipologia_lettera_list,
        'presenza_nota_di_ricezione_list': presenza_nota_di_ricezione_list,
        'presenza_indirizzo_list': presenza_indirizzo_list,
        'presenza_filigrana_list': presenza_filigrana_list,
        'presenza_sigillo_list': presenza_sigillo_list,
        'presenza_firma_list': presenza_firma_list,
        'altezza_list': altezza_list,
        'trascrittore_list': trascrittore_list,
        'larghezza_list': larghezza_list
    }

    return context


def search(request):
    context = get_context()
    query = ''
    if request.POST.get('submit') == "button1":
        print(request.POST)
        data = request.POST
        lookups = ""
        mittente_list = data.getlist('mittente')
        destinatario_list = data.getlist('destinatario')
        luogo_di_spedizione_list = data.getlist('luogo_di_spedizione')
        luogo_di_conservazione_list = data.getlist('luogo_di_conservazione')
        fondo_list = data.getlist('fondo')
        numerazione_list = data.getlist('numerazione')
        numero_prima_carta_list = data.getlist('numero_prima_carta')
        Facciata_prima_carta_list = data.getlist('Facciata_prima_carta')
        numero_totale_facciate_list = data.getlist('numero_totale_facciate')
        tipologia_lettera_list = data.getlist('tipologia_lettera')
        presenza_nota_di_ricezione_list = data.getlist('presenza_nota_di_ricezione')
        presenza_indirizzo_list = data.getlist('presenza_indirizzo')
        presenza_filigrana_list = data.getlist('presenza_filigrana')
        presenza_sigillo_list = data.getlist('presenza_sigillo')
        presenza_firma_list = data.getlist('presenza_firma')
        altezza_list = data.getlist('altezza')
        trascrittore_list = data.getlist('trascrittore')
        larghezza_list = data.getlist('larghezza')
        fromdate = data.get('fromdate')
        todate = data.get('todate')

        records = Letter.objects.all()
        if fromdate and todate:
            records = records.filter(data_di_spedizione__range=[fromdate, todate])
        if len(mittente_list) != 0:
            records = records.filter(mittente__in=mittente_list)
        if len(destinatario_list) != 0:
            records = records.filter(destinatario__in=destinatario_list)
        if len(luogo_di_spedizione_list) != 0:
            records = records.filter(luogo_di_spedizione__in=luogo_di_spedizione_list)
        if len(luogo_di_conservazione_list) != 0:
            records = records.filter(luogo_di_conservazione__in=destinatario_list)
        if len(fondo_list) != 0:
            records = records.filter(fondo__in=fondo_list)
        if len(numerazione_list) != 0:
            records = records.filter(numerazione__in=numerazione_list)
        if len(numero_prima_carta_list) != 0:
            records = records.filter(numero_prima_carta__in=numero_prima_carta_list)
        if len(Facciata_prima_carta_list) != 0:
            records = records.filter(Facciata_prima_carta__in=Facciata_prima_carta_list)
        if len(numero_totale_facciate_list) != 0:
            records = records.filter(numero_totale_facciate__in=numero_totale_facciate_list)
        if len(tipologia_lettera_list) != 0:
            records = records.filter(tipologia_lettera_in=tipologia_lettera_list)
        if len(presenza_nota_di_ricezione_list) != 0:
            records = records.filter(presenza_nota_di_ricezione__in=presenza_nota_di_ricezione_list)
        if len(presenza_indirizzo_list) != 0:
            records = records.filter(presenza_indirizzo__in=presenza_indirizzo_list)
        if len(presenza_filigrana_list) != 0:
            records = records.filter(presenza_filigrana__in=presenza_filigrana_list)
        if len(presenza_sigillo_list) != 0:
            records = records.filter(presenza_sigillo__in=presenza_sigillo_list)
        if len(presenza_firma_list) != 0:
            records = records.filter(presenza_firma__in=presenza_firma_list)
        if len(altezza_list) != 0:
            records = records.filter(altezza__in=altezza_list)
        if len(trascrittore_list) != 0:
            records = records.filter(trascrittore__in=trascrittore_list)
        if len(larghezza_list) != 0:
            records = records.filter(larghezza__in=larghezza_list)

        context.update({'records': records})
        return render(request, 'search.html', context)
    if request.POST.get('submit') == "button2":
        return render(request, 'home.html')
    if request.POST.get('submit') == "button3":
        return render(request, 'home.html')

    return render(request, 'search.html', context)
