import re
def analizza_parole(testo):
    testo_senza_punteggiatura=re.sub(r'[^\w\s]','',testo)

    parole=testo_senza_punteggiatura.split()

    occorrenze={}

    for p in parole:
        p=p.lower()
        if p in occorrenze:
            occorrenze[p]+=1
        else:
            occorrenze[p]=1
    return occorrenze

testo="Ciao, ciao! Come stai? Stai bene?"

print(analizza_parole(testo))