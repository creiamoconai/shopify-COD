import json
def blocks(prefix, items):
    b={}; order=[]
    for i,(t,s) in enumerate(items,1):
        k=f"{prefix}_{i}"; b[k]={"type":t,"settings":s}; order.append(k)
    return b,order

main_items=[
 ("for_you",{"text":"Al mattino ti vedi la pelle spenta, secca e segnata"}),
 ("for_you",{"text":"Le creme non bastano più a darti un viso idratato e luminoso"}),
 ("for_you",{"text":"La sera non hai tempo né voglia di routine lunghe"}),
 ("for_you",{"text":"Vuoi provare la skincare coreana senza spendere in istituto"}),
 ("spec",{"label":"Tipo","value":"Maschera viso notturna in idrogel, in 2 parti (fronte-occhi e guance-mento)"}),
 ("spec",{"label":"Ingredienti chiave","value":"Collagene e Centella Asiatica (INCI completo sulla confezione)"}),
 ("spec",{"label":"Tempo di posa","value":"Almeno 3 ore oppure tutta la notte"}),
 ("spec",{"label":"Frequenza","value":"2-3 volte a settimana"}),
 ("spec",{"label":"Per chi","value":"Donna e uomo, tutti i tipi di pelle"}),
 ("spec",{"label":"Nella confezione","value":"5 maschere in busta singola"}),
 ("spec",{"label":"Tipo di prodotto","value":"Cosmetico. Non è un trattamento medico"}),
 ("perk",{"text":"Le confezioni in omaggio sono già nel prezzo, nessun codice"}),
 ("perk",{"text":"Spedizione tracciata, consegna in 2-4 giorni lavorativi"}),
 ("perk",{"text":"Paghi in contanti al corriere quando ricevi il pacco"}),
 ("cross",{"product":"belliva","hook":"Vuoi completare il rituale serale?","text":"Face & Neck LED: 7 modalità di luce per viso e collo, con Siero in omaggio."}),
 ("cross",{"product":"massaggiatore-cervicale-con-calore","hook":"Collo rigido a fine giornata?","text":"Ti sdrai 10-15 minuti e lasci fare a calore e vibrazione."}),
]
mb,mo=blocks("b",main_items)
# rename keys nicer
reviews=[
 ("Pelle morbidissima al mattino","La metto prima di andare a letto e al risveglio la pelle è morbida e fresca. Mai avuta così idratata.","Paola M.","12 ottobre 2026"),
 ("Si dorme benissimo","Avevo paura di non riuscire a dormirci, invece aderisce bene e non si sposta. Al mattino la tolgo e massaggio quello che resta.","Antonella R.","11 ottobre 2026"),
 ("Il mio rituale della domenica","La uso la domenica e il mercoledì sera. Il lunedì mattina mi trucco più volentieri.","Federica L.","10 ottobre 2026"),
 ("Comoda in due parti","Essendo in due pezzi si sistema bene su fronte e guance. Facile anche per me che non sono pratica.","Gabriella T.","9 ottobre 2026"),
 ("Presa la 2+1","Ho preso l'offerta da 15 così ne ho regalata una confezione a mia figlia. Pagato alla consegna, tutto ok.","Rossella P.","8 ottobre 2026"),
 ("Effetto luminoso","Al mattino la pelle è più luminosa e uniforme, me l'ha detto anche mia sorella.","Daniela F.","7 ottobre 2026"),
 ("Profumo leggero","Non ha un profumo forte e non mi ha dato fastidio. Ho la pelle un po' sensibile e l'ho provata prima su una zona piccola.","Monica B.","6 ottobre 2026"),
 ("Consegna veloce","Arrivata in tre giorni, il corriere ha chiamato prima. Ho pagato in contanti.","Lucia G.","5 ottobre 2026"),
 ("La uso anche mio marito","Ha la pelle secca e l'ha voluta provare anche lui. Ora le finiamo il doppio più veloce!","Sabrina C.","4 ottobre 2026"),
 ("La ricompro","Sono alla seconda confezione. Per il prezzo è un piccolo lusso che mi concedo due volte a settimana.","Teresa V.","3 ottobre 2026"),
]
rb,ro=blocks("review",[("review",{"title":t,"text":x,"author":a,"stars":5}) for t,x,a,d in reviews])
hb,ho=blocks("review",[("review",{"title":t,"text":x,"author":a,"stars":5}) for t,x,a,d in reviews[:4]])
SAMPLE="ESEMPIO – da sostituire"
T={"sections":{
"main":{"type":"hv-main-offerte","blocks":mb,"block_order":mo,"settings":{
 "tag":"Skincare coreana","tag2":"Da 2,80 € a maschera",
 "subtitle":"Pelle spenta e disidratata? La metti la sera, la togli al risveglio: viso idratato, morbido e luminoso.",
 "for_heading":"Fa per te se:","gift_image":"shopify://shop_images/maschera-6-come-si-usa.jpg","preselect":2,"badge_2":"Più scelta","badge_3":"Più conveniente",
 "was_note":"Barrato = prezzo delle confezioni singole","button_label":"Ordina ora",
 "bar_text":"2+1 in omaggio · Paghi alla consegna","delivery_min":2,"delivery_max":4,
 "return_text":"14 giorni dalla consegna per il recesso (buste chiuse)",
 "cod_title":"Paghi alla consegna","cod_text":"Nessuna carta: paghi in contanti al corriere quando ricevi il pacco.",
 "cross_heading":"Completa la tua routine"}},
"highlights":{"type":"hv-highlights","blocks":hb,"block_order":ho,"settings":{"heading":"Cosa dicono le nostre clienti","sample_label":SAMPLE}},
"timeline":{"type":"hv-timeline","blocks":blocks("step",[
 ("step",{"label":"SERA 1","title":"APPLICA","points":"Pelle pulita e asciutta\nAdagi le due parti sul viso e le fai aderire\nUn minuto e sei pronta per la notte","asset":"","index":5}),
 ("step",{"label":"NOTTE","title":"LASCIA AGIRE","points":"La maschera resta in posa mentre leggi o dormi\nAlmeno 3 ore oppure tutta la notte\nNessun risciacquo, nessuno sforzo","asset":"","index":4}),
 ("step",{"label":"MATTINO","title":"RISVEGLIO","points":"Togli la maschera delicatamente\nMassaggi l'essenza rimasta fino ad assorbimento\nPelle idratata e luminosa, pronta per il trucco","asset":"","index":3})])[0],
 "block_order":["step_1","step_2","step_3"],"settings":{"eyebrow":"Come funziona","heading":"La sera la metti, al mattino la togli","text":"Nessuna routine complicata: un minuto la sera, un minuto al risveglio. Il resto lo fa la notte.","button_label":"Inizia stasera"}},
"cta":{"type":"hv-cta","settings":{"heading":"Una confezione finisce in due settimane","text":"Con l'offerta 2+1 ricevi 15 maschere a 49,90 €: un mese e mezzo di pelle idratata, a 3,33 € a maschera.","button_label":"Scegli 2+1 in omaggio","select_two":True,"note":"Pagamento alla consegna · Spedizione tracciata"}},
"band_after_cta":{"type":"hv-photo","settings":{"asset":"","index":4,"alt":"Donna a letto legge un libro con la maschera notturna","heading":"Tu leggi, dormi, ti rilassi","text":"La maschera lavora tutta la notte al posto tuo."}},
"features":{"type":"hv-features","blocks":blocks("item",[
 ("item",{"icon":"drop","title":"Pelle secca?","text":"Idratazione che dura tutta la notte."}),
 ("item",{"icon":"light","title":"Viso spento?","text":"Al mattino è più luminoso e uniforme."}),
 ("item",{"icon":"clock","title":"Poco tempo?","text":"Un minuto la sera, un minuto al mattino."}),
 ("item",{"icon":"hand","title":"Maschere che scivolano?","text":"L'idrogel in 2 parti aderisce e resta al suo posto."}),
 ("item",{"icon":"home","title":"Istituto costoso?","text":"Skincare coreana a casa, da 2,80 € a maschera."})])[0],
 "block_order":["item_1","item_2","item_3","item_4","item_5"],"settings":{"band":"Maschera notturna • Collagene • Centella Asiatica • Paghi alla consegna","heading":"","text":"","grey":False}},
"numbers":{"type":"hv-numbers","blocks":blocks("stat",[
 ("stat",{"number":"1","unit":"minuto","fill":20,"title":"Per applicarla","text":"Due parti da adagiare sul viso, e hai finito."}),
 ("stat",{"number":"3+","unit":"ore","fill":60,"title":"In posa","text":"Almeno 3 ore, meglio tutta la notte."}),
 ("stat",{"number":"2-3","unit":"a settimana","fill":45,"title":"Frequenza","text":"Bastano poche sere per una routine costante."}),
 ("stat",{"number":"15","unit":"maschere","fill":100,"title":"Con il 2+1","text":"Un mese e mezzo di routine notturna."})])[0],
 "block_order":["stat_1","stat_2","stat_3","stat_4"],"settings":{"heading":"La maschera in numeri","text":"Poco sforzo, tanta costanza: è questo il segreto della skincare coreana.","asset":"","index":2}},
"tips":{"type":"hv-tips","blocks":blocks("tip",[
 ("tip",{"tip":"Struccati, lava il viso e asciugalo bene: su pelle pulita la maschera aderisce meglio.","title":"Detergi","signature":"","icon":"drop"}),
 ("tip",{"tip":"Adagia prima la parte superiore, poi quella inferiore, e premi con le dita perché aderiscano.","title":"Applica","signature":"","icon":"hand"}),
 ("tip",{"tip":"Lasciala in posa almeno 3 ore o tutta la notte, finché diventa sottile e trasparente.","title":"Lascia agire","signature":"","icon":"clock"}),
 ("tip",{"tip":"Al mattino toglila e massaggia l'essenza rimasta fino ad assorbimento. Prima volta? Prova su una piccola zona.","title":"Massaggia","signature":"","icon":"heart"})])[0],
 "block_order":["tip_1","tip_2","tip_3","tip_4"],"settings":{"heading":"Come si usa, in 4 passi","text":"Segui sempre le indicazioni riportate sulla confezione."}},
"cards":{"type":"hv-cards","blocks":blocks("card",[
 ("card",{"title":"Idrogel in 2 parti","tags":"Design, Uso","points":"Fronte e occhi\nGuance e mento","details":"Due pezzi separati si adattano a ogni viso e aderiscono senza scivolare.","asset":"","index":2}),
 ("card",{"title":"Collagene","tags":"Ingredienti","points":"Classico della skincare coreana\nIdrata e ammorbidisce","details":"Il collagene aiuta a mantenere la pelle idratata e morbida al tatto.","asset":"","index":1}),
 ("card",{"title":"Centella Asiatica","tags":"Ingredienti","points":"Lenitiva\nAmata in Corea","details":"Un ingrediente tradizionale della cosmesi coreana, delicato sulla pelle.","asset":"","index":5}),
 ("card",{"title":"Effetto trasparente","tags":"Uso","points":"Diventa sottile e trasparente\nCosì sai quando è pronta","details":"Durante la posa la maschera rilascia l'essenza e si assottiglia: è il segnale che ha lavorato.","asset":"","index":4}),
 ("card",{"title":"Busta singola","tags":"Comodità","points":"Igienica\nPerfetta anche in viaggio","details":"Ogni maschera ha la sua busta: ne apri una alla volta, sempre fresca.","asset":"","index":3}),
 ("card",{"title":"Per lei e per lui","tags":"Uso","points":"Tutti i tipi di pelle\nDa condividere","details":"Cosmetico per la routine di bellezza. Non è un trattamento medico.","asset":"","index":6})])[0],
 "block_order":[f"card_{i}" for i in range(1,7)],"settings":{"heading":"Cosa c'è dentro la maschera","text":"Pochi ingredienti scelti, una formula pensata per la notte."}},
"band_after_cards":{"type":"hv-photo","settings":{"asset":"","index":3,"alt":"Donna allo specchio sistema la maschera sul viso","heading":"Al mattino, uno sguardo diverso allo specchio","text":"Pelle idratata e luminosa, prima ancora del trucco."}},
"perks":{"type":"hv-features","blocks":blocks("item",[
 ("item",{"icon":"cash","title":"Pagamento alla consegna","text":"Compili il modulo e paghi in contanti al corriere quando ricevi il pacco."}),
 ("item",{"icon":"truck","title":"Spedizione tracciata","text":"Consegna in 2-4 giorni lavorativi, con numero di tracciamento."}),
 ("item",{"icon":"return","title":"14 giorni per il recesso","text":"Hai 14 giorni dalla consegna. Per igiene, solo buste chiuse."}),
 ("item",{"icon":"chat","title":"Assistenza in italiano","text":"Ti rispondiamo noi, prima e dopo l'acquisto."}),
 ("item",{"icon":"heart","title":"Omaggi già inclusi","text":"Con 2+1 e 3+2 il prezzo che vedi è già quello finale, senza codici."}),
 ("item",{"icon":"shield","title":"Nessun dato di carta","text":"Ordini senza inserire carte: paghi solo quando hai il pacco in mano."})])[0],
 "block_order":[f"item_{i}" for i in range(1,7)],"settings":{"band":"","heading":"Perché ordinare su Belliva","text":"","grey":True}},
"image_text":{"type":"hv-image-text","settings":{"eyebrow":"Il tuo momento","heading":"La skincare che lavora mentre dormi","text":"<p>Niente routine da dieci passaggi. La sera, dopo la doccia, adagi la maschera e ti metti a letto. Al mattino la togli, massaggi l'essenza e sei pronta. Semplice, costante, tutta per te.</p>","button_label":"Ordina ora","button_link":"","reverse":True,"grey":False,"asset":"","index":5}},
"compare":{"type":"hv-compare","blocks":blocks("x",[
 ("tab",{"title":"Casa o istituto?","text":"<p>Un trattamento viso in istituto ha il valore della consulenza di un professionista. La maschera notturna ti dà un gesto semplice, a casa, mentre dormi.</p>","index":1}),
 ("tab",{"title":"Cosa ricevi","text":"<p>Ogni confezione contiene 5 maschere in busta singola. Con il 2+1 ricevi 3 confezioni (15 maschere), con il 3+2 ne ricevi 5 (25 maschere).</p>","index":6}),
 ("tab",{"title":"Pagamento e consegna","text":"<p>Paghi alla consegna, in contanti al corriere. La spedizione è tracciata e arriva in 2-4 giorni lavorativi.</p>","index":0}),
 ("row",{"feature":"Lavora mentre dormi","us":True,"them":False}),
 ("row",{"feature":"Nessun appuntamento da prenotare","us":True,"them":False}),
 ("row",{"feature":"Meno di 3,50 € a maschera con il 2+1","us":True,"them":False}),
 ("row",{"feature":"Niente spostamenti","us":True,"them":False}),
 ("row",{"feature":"Pagamento alla consegna","us":True,"them":False}),
 ("row",{"feature":"Valutazione di un professionista","us":False,"them":True})])[0],
 "block_order":None,"settings":{"heading":"La maschera a confronto","us_label":"Maschera a casa","them_label":"In istituto"}},
"gallery":{"type":"hv-gallery","blocks":blocks("photo",[("photo",{"asset":"","index":i}) for i in [1,4,2,3,5,6]])[0],
 "block_order":[f"photo_{i}" for i in range(1,7)],"settings":{"heading":"Il rituale notturno Belliva","text":"La tua skincare, mentre dormi."}},
"reviews":{"type":"hv-reviews","blocks":rb,"block_order":ro,"settings":{"heading":"Recensioni clienti","sample_label":SAMPLE,"empty_title":"Sii la prima a recensirla","empty_text":"Pubblichiamo solo recensioni di clienti che l'hanno acquistata davvero. Dopo la consegna ti scriviamo per chiederti com'è andata."}},
"band_before_faq":{"type":"hv-photo","settings":{"asset":"","index":2,"alt":"Primo piano della maschera in idrogel sul viso","heading":"Aderisce come una seconda pelle","text":"Pagamento alla consegna e spedizione tracciata."}},
"faq":{"type":"hv-faq","blocks":blocks("question",[
 ("question",{"question":"Come funziona l'offerta 2+1?","answer":"<p>Scegli «2+1 in OMAGGIO»: ricevi 3 confezioni (15 maschere) e paghi 49,90 €. Con «3+2» ricevi 5 confezioni (25 maschere) a 69,90 €. Il prezzo che vedi è già quello finale.</p>"}),
 ("question",{"question":"Devo tenerla tutta la notte?","answer":"<p>È pensata per la notte, ma se preferisci puoi tenerla almeno 3 ore e toglierla prima di dormire.</p>"}),
 ("question",{"question":"Quanto spesso posso usarla?","answer":"<p>Consigliamo 2-3 volte a settimana. Una confezione da 5 dura circa due settimane.</p>"}),
 ("question",{"question":"Va bene per la pelle sensibile?","answer":"<p>Prima del primo utilizzo fai una prova su una piccola zona. Non applicarla su pelle irritata o lesa. In caso di arrossamento toglila e risciacqua. L'elenco completo degli ingredienti è sulla confezione.</p>"}),
 ("question",{"question":"Come posso pagare?","answer":"<p>Paghi alla consegna: compili il modulo d'ordine e paghi in contanti al corriere quando ricevi il pacco.</p>"}),
 ("question",{"question":"Quanto ci mette ad arrivare?","answer":"<p>La spedizione è tracciata e arriva di solito in 2-4 giorni lavorativi. Ricevi il numero di tracciamento appena il pacco parte.</p>"}),
 ("question",{"question":"Posso restituirla?","answer":"<p>Hai 14 giorni dalla consegna per il recesso. Trattandosi di un cosmetico, per motivi igienici accettiamo solo buste sigillate e non aperte.</p>"})])[0],
 "block_order":[f"question_{i}" for i in range(1,8)],"settings":{"heading":"Domande frequenti"}}
},
"order":["main","highlights","timeline","cta","band_after_cta","features","numbers","tips","cards","band_after_cards","perks","image_text","compare","gallery","reviews","band_before_faq","faq"]}
# fix compare keys to tab_/row_ like original
cb={};co=[]
for i,(k,v) in enumerate(T["sections"]["compare"]["blocks"].items(),1):
    nk=f"{v['type']}_{i}"; cb[nk]=v; co.append(nk)
T["sections"]["compare"]["blocks"]=cb; T["sections"]["compare"]["block_order"]=co
# main block keys like original
nb={};no=[];cnt={}
for k in mo:
    v=mb[k]; cnt[v['type']]=cnt.get(v['type'],0)+1; nk=f"{v['type']}_{len(no)+1}"; nb[nk]=v; no.append(nk)
T["sections"]["main"]["blocks"]=nb; T["sections"]["main"]["block_order"]=no
for s in T["sections"].values():
    if "blocks" in s and s.get("block_order") is not None: assert set(s["block_order"])==set(s["blocks"]),s["type"]
json.dump(T,open('/home/user/shopify-COD/theme/templates/product.maschera.json','w'),ensure_ascii=False,indent=2)
print(json.dumps(json.dumps(T,ensure_ascii=True,separators=(',',':'))))
