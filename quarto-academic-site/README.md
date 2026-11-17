# Personlig akademisk nettside – Quarto

Dette er et førsteutkast, ikke en publisert nettside. Kildematerialet er seks
Quarto-sider med felles design, navigasjon og oppsett.

## Prøv ut nettsiden

1. Pakk ut ZIP-filen på PC-en.
2. Åpne `preview/index.html` i nettleseren for en offline visning av førsteutkastet.
   Visningen er laget fra de samme QMD-filene ved hjelp av Pandoc, og er ikke
   en eksakt Quarto-render.
3. Installer [Quarto](https://quarto.org/docs/get-started/) og åpne prosjektmappen i VS Code.
4. Fra terminalen i prosjektmappen:

       quarto preview

   Quarto åpner nettstedet og oppdaterer forhåndsvisningen når du lagrer endringer.

5. Når du er fornøyd, genererer du nettstedet med:

       quarto render

   Den ferdige nettsiden ligger i `_site/`.

## Før publisering

- NTNU-portrettet er lagt inn i `assets/portrait.jpg`. Bytt gjerne ut filen dersom du ønsker et annet foto senere.
- Gå gjennom stillingstitler og førsteutkastet til biografien.
- Gå gjennom publikasjonslisten, de pågående paperne og den tematiske rapportoversikten.
- Den oppdaterte CV-en er allerede lagt inn i `assets/cv.pdf`, og lenket på forsiden og CV-siden. Erstatt filen med en ny PDF ved senere oppdatering.
- Google Scholar-lenken viser foreløpig et publikasjonsøk. Erstatt med direkte profiladresse når den er bekreftet, og legg eventuelt inn ORCID.

## Redigering

| Fil | Innhold |
|---|---|
| index.qmd | Forside, biografi og utvalgt forskning |
| research.qmd | Vitenskapelige publikasjoner |
| projects.qmd | Forskningsprosjekter |
| applied-research.qmd | Anvendt forskning og rapporter |
| teaching.qmd | Kort undervisningsprofil |
| cv.qmd | CV og kontaktopplysninger |
| _quarto.yml | Menyer og globale innstillinger |
| styles.css | Farger, typografi og layout |

## Publiser med GitHub Pages

1. Opprett en konto på [GitHub](https://github.com/) og et offentlig repository
   med navnet `DITT-BRUKERNAVN.github.io` (bruk ditt faktiske brukernavn).
2. Installer [GitHub Desktop](https://desktop.github.com/) og klon repositoriet.
3. Kopier innholdet i denne Quarto-prosjektmappen (inkludert `.github/` og
   `.gitignore`) til den klonede mappen. Ikke kopier selve ZIP-filen.
4. I GitHub Desktop: velg *Commit to main* og deretter *Push origin*.
5. På GitHub: åpne repositoriet, velg *Settings → Pages → Source → GitHub Actions*.
6. Under *Actions* kan du velge *Build and publish Quarto website* og *Run workflow*
   dersom den ikke kjører automatisk, eller hvis første kjøring skjedde før Pages ble aktivert.
7. Når arbeidsflyten er grønn, finner du nettadressen i *Settings → Pages*.

Arbeidsflyten er inkludert i `.github/workflows/deploy.yml`. Den bygger nettsiden
med Quarto og publiserer kun den genererte HTML-nettsiden og tilhørende filer.
Fremtidige endringer i QMD-filer som pushes til GitHub publiseres automatisk.
Se [GitHub Pages-dokumentasjonen](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

