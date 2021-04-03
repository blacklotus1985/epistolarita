# Create your views here.
import xlrd
import json
from django.shortcuts import redirect,render
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import send_mail
#jsonDec = json.decoder.JSONDecoder()
#myPythonList = jsonDec.decode(attr)

from .models import Letter, Recommender, Statistic,TempLetter

path = r'C:\Users\black\OneDrive\Desktop\Alex\github_projects\belgium\versions\src\src\tables.xlsx'
def Insert_Letter(request):
    loc = (path)

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(2, sheet.nrows):
        data = sheet.row_values(i)
        object = Letter.objects.create(
            id_lettera=data[0],
            mittente=data[1],
            destinatario=data[2],
            luogo_di_spedizione=data[3],
            data_di_spedizione=data[4],
            luogo_di_conservazione=data[5],
            fondo=data[6],
            numerazione=data[7],
            numero_prima_carta=data[8],
            Facciata_prima_carta=data[9],
            numero_totale_facciate=data[10],
            tipologia_lettera=data[11],
            presenza_nota_di_ricezione=data[12],
            presenza_indirizzo=data[13],
            presenza_filigrana=data[14],
            presenza_sigillo=data[15],
            presenza_firma=data[16],
            altezza=data[17],
            larghezza=data[18],
            dimensioni=json.dumps(data[19]),
            trascrittore=data[20],
            testo=data[21],
        )
    return redirect("/")


def Insert_Recommender(request):
    loc = (path)

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(1)
    for i in range(2, sheet.nrows):
        data = sheet.row_values(i)
        object = Recommender.objects.create(
            id_lettera=data[0],
            similar_ID= json.dumps(data[1]),
            similarity_value=json.dumps(data[2])
        )
    return redirect("/")


def Insert_Statistic(request):
    loc = (path)

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(2)
    for i in range(2, sheet.nrows):
        data = sheet.row_values(i)
        object = Statistic.objects.create(
            id_lettera=data[0],
            top_words=json.dumps(data[1]),
            n_words=data[2]
        )
    return redirect("/")

def send_confirmation():
    context = {}
    txt_ = get_template("notify.txt").render(context)
    html_ = get_template("notify.html").render(context)
    subject = 'New Letter Added!!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['vijaykushal8118@gmail.com']
    sent_mail = send_mail(
        subject,
        txt_,
        from_email,
        recipient_list,
        html_message=html_,
        fail_silently=False,
    )
    return sent_mail

def AddLetter(request):

    if request.method == 'POST':
        data = request.POST
        id_lettera = str(data['luogo_di_spedizione']) + "_" + str(data['fondo']) + "_"
        cnt  = Letter.objects.filter(id_lettera__icontains=id_lettera).count()
        id_lettera += str(cnt + 1)
        object = TempLetter.objects.create(
            id_lettera=id_lettera,
            mittente=data['mittente'],
            destinatario=data['destinatario'],
            luogo_di_spedizione=data['luogo_di_spedizione'],
            data_di_spedizione=data['data_di_spedizione'],
            luogo_di_conservazione=data['luogo_di_conservazione'],
            fondo=data['fondo'],
            numerazione=data['numerazione'],
            numero_prima_carta=data['numero_prima_carta'],
            Facciata_prima_carta=data['Facciata_prima_carta'],
            numero_totale_facciate=data['numero_totale_facciate'],
            tipologia_lettera=data['tipologia_lettera'],
            presenza_nota_di_ricezione=data['presenza_nota_di_ricezione'],
            presenza_indirizzo=data['presenza_indirizzo'],
            presenza_filigrana=data['presenza_filigrana'],
            presenza_sigillo=data['presenza_sigillo'],
            presenza_firma=data['presenza_firma'],
            altezza=data['altezza'],
            larghezza=data['larghezza'],
            dimensioni=json.dumps(data['dimensioni']),
            trascrittore=data['trascrittore'],
            testo=data['testo'],
        )
        send_confirmation()
        return redirect("/")
    return render(request,'addletter.html')
