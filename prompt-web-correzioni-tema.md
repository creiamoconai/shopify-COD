Devi correggere dei testi nel mio tema Shopify. Lavora SOLO sul tema di prova, NON sul tema pubblicato.

DATI
- Tema su cui lavorare: "PROVA maschera (non pubblicare)" → gid://shopify/OnlineStoreTheme/202625745223
- NON toccare il tema pubblicato "Belliva v20 — Card prezzi" (202428711239). Non pubblicare nessun tema.
- Usa themeFilesUpsert solo sul tema 202625745223.

PRIMA DI TUTTO: leggi i file templates/product.belliva.json, templates/product.anticellulite.json, templates/product.cervicale.json del tema 202625745223 e mostrami dove compaiono i prezzi e le recensioni. Poi fai le modifiche qui sotto, mantenendo IDENTICO tutto il resto del file (stessa struttura JSON, stessi blocchi, stesse impostazioni).

PREZZI ATTUALI (veri, in Shopify):
- Face & Neck LED: 1 pezzo 49,90 € · 2 pezzi 74,90 € (invece di 99,80 €)
- Anticellulite 4in1: 1 pezzo 49,90 € · 2 pezzi 74,90 € (invece di 99,80 €)
- Cervicale: 59,90 €

MODIFICA 1 – Prezzi vecchi nei testi
In tutti e 3 i template cerca ogni testo con prezzi vecchi e aggiornalo:
- "79,90 €" → "74,90 €"
- "109,80 €" → "99,80 €"
- nel template cervicale "69,90 €" → "59,90 €"
Controlla in particolare la sezione "cta" (campo text) e la sezione "faq" (prima domanda). Se trovi altri prezzi, mostrameli prima di cambiarli.

MODIFICA 2 – Recensioni non reali
Le recensioni nei template sono di esempio (scritte prima che arrivassero ordini veri) e alcune hanno l'etichetta "acquisto verificato". Non è legale mostrarle come vere.
In tutti e 3 i template:
- nella sezione "reviews": svuota "blocks" ({}) e "block_order" ([]), metti "sample_label": "". Così la pagina mostra il riquadro "Hai già provato…? Raccontaci la tua esperienza".
- nella sezione "highlights" (se esiste): rimuovi "highlights" dall'array "order" del template (non cancellare la sezione, toglila solo dall'ordine).

MODIFICA 3 – Controllo finale
Rileggi i 3 file dopo il salvataggio e dammi una tabella: file, cosa hai cambiato (prima → dopo), eventuali errori.

REGOLE
- Non inventare recensioni, non aggiungere testi nuovi, non cambiare prezzi dei prodotti.
- Non toccare il template product.maschera.json né la sezione hv-main-offerte.liquid.
- Se un salvataggio dà errore, fermati e dimmi l'errore.
