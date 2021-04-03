from django.db import models


BINARY_CHOICES = (
    (0.0, 0.0),
    (1.0, 1.0),
)
Facciata_prima_carta_CHOICES = (
    ("r", "r"),
    ("v", "v"),
)
tipologia_lettera_CHOICES = (
    ("copia", "copia"),
    ("originale", "originale"),
)
# Create your models here.
class Letter(models.Model):
    id_lettera = models.CharField(max_length=255, unique=True)
    mittente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    luogo_di_spedizione = models.CharField(max_length=255)
    data_di_spedizione = models.DateField(auto_now=True)
    luogo_di_conservazione = models.CharField(max_length=255)
    fondo = models.CharField(max_length=255)
    numerazione = models.FloatField(choices=BINARY_CHOICES)
    numero_prima_carta = models.IntegerField()
    Facciata_prima_carta = models.CharField(max_length=1, choices=Facciata_prima_carta_CHOICES)
    numero_totale_facciate = models.IntegerField()
    tipologia_lettera = models.CharField(max_length=255,choices=tipologia_lettera_CHOICES)
    presenza_nota_di_ricezione = models.FloatField(choices=BINARY_CHOICES)
    presenza_indirizzo = models.FloatField(choices=BINARY_CHOICES)
    presenza_filigrana = models.FloatField(choices=BINARY_CHOICES)
    presenza_sigillo = models.FloatField(choices=BINARY_CHOICES)
    presenza_firma = models.FloatField(choices=BINARY_CHOICES)
    altezza = models.IntegerField()
    larghezza = models.IntegerField()
    dimensioni = models.TextField()
    trascrittore = models.CharField(max_length=255)
    testo = models.TextField()

    def __str__(self):
        return self.id_lettera


class Recommender(models.Model):
    id_lettera = models.CharField(max_length=255, unique=True)
    similar_ID = models.TextField()
    similarity_value = models.TextField()

    def __str__(self):
        return self.id_lettera


class Statistic(models.Model):
    id_lettera = models.CharField(max_length=255, unique=True)
    top_words = models.TextField()
    n_words = models.IntegerField()

    def __str__(self):
        return self.id_lettera

class TempLetter(models.Model):
    id_lettera = models.CharField(max_length=255, unique=True)
    mittente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    luogo_di_spedizione = models.CharField(max_length=255)
    data_di_spedizione = models.DateField(auto_now=True)
    luogo_di_conservazione = models.CharField(max_length=255)
    fondo = models.CharField(max_length=255)
    numerazione = models.FloatField(choices=BINARY_CHOICES)
    numero_prima_carta = models.IntegerField()
    Facciata_prima_carta = models.CharField(max_length=1, choices=Facciata_prima_carta_CHOICES)
    numero_totale_facciate = models.IntegerField()
    tipologia_lettera = models.CharField(max_length=255,choices=tipologia_lettera_CHOICES)
    presenza_nota_di_ricezione = models.FloatField(choices=BINARY_CHOICES)
    presenza_indirizzo = models.FloatField(choices=BINARY_CHOICES)
    presenza_filigrana = models.FloatField(choices=BINARY_CHOICES)
    presenza_sigillo = models.FloatField(choices=BINARY_CHOICES)
    presenza_firma = models.FloatField(choices=BINARY_CHOICES)
    altezza = models.IntegerField()
    larghezza = models.IntegerField()
    dimensioni = models.TextField()
    trascrittore = models.CharField(max_length=255)
    testo = models.TextField()
    corrected = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.corrected:
            if Letter.objects.filter(id_lettera=self.id_lettera).exists():
                object = Letter.objects.filter(id_lettera=self.id_lettera).update(
                    mittente=self.mittente,
                    destinatario=self.destinatario,
                    luogo_di_spedizione=self.luogo_di_spedizione,
                    data_di_spedizione=self.data_di_spedizione,
                    luogo_di_conservazione=self.luogo_di_conservazione,
                    fondo=self.fondo,
                    numerazione=self.numerazione,
                    numero_prima_carta=self.numero_prima_carta,
                    Facciata_prima_carta=self.Facciata_prima_carta,
                    numero_totale_facciate=self.numero_totale_facciate,
                    tipologia_lettera=self.tipologia_lettera,
                    presenza_nota_di_ricezione=self.presenza_nota_di_ricezione,
                    presenza_indirizzo=self.presenza_indirizzo,
                    presenza_filigrana=self.presenza_filigrana,
                    presenza_sigillo=self.presenza_sigillo,
                    presenza_firma=self.presenza_firma,
                    altezza=self.altezza,
                    larghezza=self.larghezza,
                    dimensioni=self.dimensioni,
                    trascrittore=self.trascrittore,
                    testo=self.testo,
                )
            else:
                object = Letter.objects.create(
                    id_lettera=self.id_lettera,
                    mittente=self.mittente,
                    destinatario=self.destinatario,
                    luogo_di_spedizione=self.luogo_di_spedizione,
                    data_di_spedizione=self.data_di_spedizione,
                    luogo_di_conservazione=self.luogo_di_conservazione,
                    fondo=self.fondo,
                    numerazione=self.numerazione,
                    numero_prima_carta=self.numero_prima_carta,
                    Facciata_prima_carta=self.Facciata_prima_carta,
                    numero_totale_facciate=self.numero_totale_facciate,
                    tipologia_lettera=self.tipologia_lettera,
                    presenza_nota_di_ricezione=self.presenza_nota_di_ricezione,
                    presenza_indirizzo=self.presenza_indirizzo,
                    presenza_filigrana=self.presenza_filigrana,
                    presenza_sigillo=self.presenza_sigillo,
                    presenza_firma=self.presenza_firma,
                    altezza=self.altezza,
                    larghezza=self.larghezza,
                    dimensioni= self.dimensioni,
                    trascrittore=self.trascrittore,
                    testo=self.testo,
                )
        super(TempLetter, self).save(*args, **kwargs)

    def __str__(self):
        return self.id_lettera
