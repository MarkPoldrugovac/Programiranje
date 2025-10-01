kosarica={}
print(f"Prazna košarica: {kosarica}")
print(f"Tip{type(kosarica)}")

kosarica['jabuka']=15
kosarica['kreke']=23
kosarica['mandarine']=3

print(f"Napunjena košarica:{kosarica}")

kosarica['jabuka']=kosarica['jabuka']+5
print(f"Ažurirana košarica:{kosarica}")

broj_mandarina=kosarica['mandarine']
print(f"Broj mandarina:{broj_mandarina}")

try:
    broj_krusaka=krusaka['kruska']
    print(f"Broj krusaka:{broj_krusaka}")
except Exception as e:
    print(f"Greška:{e}")

trazim_voce='kruska'
if trazim_voce in kosarica:
    print(f"Imamo{kosarica[trazim_voce]}komada voća")
