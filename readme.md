# Data But Make It Everything IT

AI-drevet trendanalysesystem for informasjonssystemer. Kombinerer data fra Google Trends, Reddit og teknologinyheter for å identifisere og analysere emerging IT-trender med et sosioteknisk perspektiv.

# Google Trends Data Collection

## 📌 Status per august 2025
Prosjektet er i gang med innhenting og visualisering av Google Trends-data ved hjelp av `pytrends`.  
Målet er å hente søketrender for relevante teknologiske nøkkelord og analysere utviklingen over tid.

---

## ✅ Gjort så langt
- Opprettet Python-script (`google_trends.py`) som:
  - Henter trender for flere nøkkelord (`AI`, `Blockchain technology`, `Cloud services`)
  - Oppdager og løser problemet med manglende variasjon ved å hente søkeord separat og normalisere dataene
  - Lagrer resultatene til `data/google_trends.csv`
  - Plotter dataene direkte med `matplotlib` for rask visuell inspeksjon
- Testet at datasettet nå inneholder meningsfull variasjon for alle søkeord

---

## 📊 Foreløpig resultat
Trenden viser:
- **AI**: Kraftig vekst siste to år
- **Blockchain technology**: Flere tydelige topper, men generelt mer volatil interesse
- **Cloud services**: Jevnere interesse med gradvis økning





---

## 📥 Datakilder
- Google Trends
- Reddit (r/technology, r/MachineLearning, osv.)
- NewsAPI (tech news)

## 🧠 Teknologier brukt
- Python (Pandas, PRAW, PyTrends)
- scikit-learn (TF-IDF / LDA)
- Matplotlib

## 🎯 Formål
Dette prosjektet inngår i emnet *Emerging Trends in Information Systems*.

