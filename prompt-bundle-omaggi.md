# Bundle con doppio omaggio – EasySell, copy e creative

Da attivare DOPO il test (non prima di mercoledì 21 ottobre) e SOLO quando:
- il fornitore ha confermato notifica CPNP + persona responsabile UE + etichetta in italiano del rossetto
- lo stock di rossetti (30-40 pz) è arrivato al magazzino CODfacile

## Le offerte

| Offerta | Prezzo | Omaggio |
|---|---|---|
| LED singolo | 49,90 € | siero (come oggi) |
| **LED x2** | 79,90 € | **2 sieri + rossetto magico** |
| Maschera 1 confezione | 29,90 € | nessuno |
| **Maschera 2+1** | 49,90 € | **rossetto magico** |
| **Maschera 5 confezioni** | 69,90 € | **rossetto magico** |

Costi rossetto: 1,50 € al pezzo. Margine LED x2 ≈ 49 € (contro 29 € del singolo).

---

## 1. PROMPT PER CLAUDE WEB – configurazione EasySell

```
Ciao, ho un negozio Shopify (belliva.it) con pagamento alla consegna tramite l'app EasySell COD Form.
Devo impostare delle offerte a quantità con omaggio. Guidami passo passo, schermata per schermata, senza dare nulla per scontato. Non inviare mai il modulo d'ordine per fare prove.

PASSO 0 – Prodotto omaggio su Shopify
Crea su Shopify un prodotto "Rossetto Magico (OMAGGIO)" a 0 €, con SKU dedicato, nascosto dal negozio (non visibile nelle collezioni), come già esiste "Siero Acido Ialuronico (OMAGGIO)". Serve perché CODfacile sappia di metterlo nel pacco.

PASSO 1 – Prodotto "Belliva Face & Neck LED" (pagina /products/belliva)
In EasySell > Offerte a quantità (Quantity offers) imposta:
- 1 pezzo: 49,90 € – testo: "🎁 Siero in omaggio"
- 2 pezzi: 79,90 € – titolo: "2 Belliva – uno per te, uno da regalare" – testo: "🎁 2 sieri + rossetto magico in OMAGGIO" – etichetta "Il più scelto" – PRESELEZIONATA
Verifica se EasySell permette di aggiungere automaticamente un prodotto omaggio all'offerta (gift/free product). Se sì, collega all'offerta da 2: Siero (OMAGGIO) x2 + Rossetto Magico (OMAGGIO) x1. Se no, dimmelo e troviamo il modo di far comparire gli omaggi nell'ordine (es. nota sull'ordine) così CODfacile li vede.

PASSO 2 – Prodotto "Maschera Bio-Collagene Notturna" (pagina /products/maschera-bio-collagene-notturna)
Offerte a quantità:
- 1 confezione: 29,90 € – nessun omaggio
- 2+1 (3 confezioni): 49,90 € – testo: "🎁 Rossetto magico in OMAGGIO" – etichetta "Il più scelto" – PRESELEZIONATA
- 5 confezioni: 69,90 € – testo: "🎁 Rossetto magico in OMAGGIO · Miglior prezzo"
Collega il Rossetto Magico (OMAGGIO) x1 alle offerte 2+1 e 5 confezioni (stesso discorso del passo 1).

PASSO 3 – Non toccare
- Non modificare l'upsell "LED - Maschere Bio-Collagene 14,90" già attivo.
- Non modificare impostazioni di pixel / tracciamento.

PASSO 4 – Verifica
Dimmi come controllare dall'anteprima (senza inviare ordini) che:
- l'offerta preselezionata sia quella giusta
- i prezzi totali siano corretti
- il testo degli omaggi sia visibile su telefono
Alla fine fammi un riepilogo di cosa è stato modificato.
```

---

## 2. COPY INSERZIONI (senza prezzi)

### LED – "Doppio regalo"
Testo principale:
```
Uno per te, uno da regalare 🎁

Belliva Face & Neck: 7 luci LED per la tua coccola viso e collo, 10 minuti la sera, comodamente a casa.

Scegli la confezione da 2 e ricevi in OMAGGIO:
✔️ 2 sieri all'acido ialuronico
✔️ il rossetto magico che cambia colore

🚚 Spedizione gratuita
💶 Paghi in contanti alla consegna

👉 Ordina ora, gli omaggi sono già inclusi
```
Titolo: `Uno per te, uno da regalare 🎁`
Pulsante: Ordina ora · Link: https://belliva.it/products/belliva

### Maschera – "Il regalo in più"
Testo principale:
```
15 notti di pelle morbida e luminosa ✨

La sera applichi la maschera al collagene, al mattino la togli. Nessun risciacquo.

Scegli il pacchetto 2+1 o da 5 confezioni e ricevi IN OMAGGIO il rossetto magico che cambia colore 💄

🚚 Spedizione gratuita
💶 Paghi in contanti alla consegna

👉 Ordina ora, il regalo è già incluso
```
Titolo: `Pacchetto + rossetto in omaggio 💄`
Pulsante: Ordina ora · Link: https://belliva.it/products/maschera-bio-collagene-notturna

---

## 3. PROMPT IMMAGINI (ChatGPT / Gemini) – senza prezzi

REGOLE per tutte:
- Allega SEMPRE le foto reali di: dispositivo LED / confezione maschera / siero / rossetto. Il prodotto deve essere identico all'originale.
- Niente prezzi, niente prima/dopo, niente promesse mediche, niente "botox".
- "Omaggio" scritto UNA sola volta per immagine.
- Testi in italiano, grandi e leggibili da telefono. Formato 4:5 (1080x1350).

### Statica LED – "Doppio regalo"
```
Crea un'immagine pubblicitaria verticale 4:5 per Facebook e Instagram, stile fotografico realistico, luce calda natalizia ma elegante (niente Babbo Natale).
Al centro, su un tavolino in legno chiaro con una coperta beige, due apparecchi per viso e collo identici a quelli dell'immagine allegata (bianchi a forma di T, luci LED rosse accese), uno dentro una scatola regalo aperta con fiocco rosa cipria.
Davanti, in primo piano: due flaconcini di siero identici a quello allegato e un rossetto trasparente con fiocchi dorati identico a quello allegato.
In alto titolo grande: "Uno per te, uno da regalare".
In basso fascia arrotondata rosa cipria con testo bianco: "2 sieri + rossetto magico in omaggio · Paghi alla consegna".
```

### Statica Maschera – "Pacchetto + rossetto"
```
Crea un'immagine pubblicitaria verticale 4:5 per Facebook e Instagram, stile fotografico realistico, luce morbida della sera, bagno elegante color crema.
Al centro tre confezioni di maschera identiche a quella allegata, disposte a ventaglio. Accanto, un rossetto trasparente con fiocchi dorati identico a quello allegato, appoggiato su un piattino dorato, con un piccolo fiocco.
Sullo sfondo, sfocata, una donna italiana sui 45 anni in accappatoio che sorride guardandosi allo specchio.
In alto titolo grande: "15 notti di pelle luminosa".
In basso fascia arrotondata malva con testo bianco: "Rossetto magico in omaggio con il pacchetto".
```

---

## COME SI CARICANO
- LED: nuova inserzione nel gruppo G1 (non nuovo gruppo).
- Maschera: nuova inserzione nel gruppo G4.
- Stessa regola: 25 € spesi senza ordini → si spegne.
