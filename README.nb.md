# Tur Home Assistant – beta

[Norsk](README.nb.md) | [English](README.md)

> **BETA – aktiv utvikling. Ikke et gjennomtestet produkt. Ingen installerbar integrasjon er publisert ennå.**

Tur-integrasjonen skal vise dine egne, godkjente aktivitetstall i Home Assistant. Den utvikles sammen med neste beta av [Tur for Android](https://github.com/trondtorsoe/Tur-Activity-Tracker-for-Android).

## Ikonoversikt

Symbolene gjenbruker appens ikonformer og farger.

| Ikon fra appen | Funksjon i integrasjonen |
|---|---|
| <img src="docs/icons/key.svg" width="56" height="56" alt="Nøkkel"> | **Nøkkel og tilgang** – opprett, kopier og trekk tilbake egen delingsnøkkel. |
| <img src="docs/icons/sharing.svg" width="56" height="56" alt="Deling"> | **Deling** – velg hvilke av dine aktivitetstall som kan leses. |
| <img src="docs/icons/groups.svg" width="56" height="56" alt="Grupper"> | **Grupper** – egen lederstatus per gruppe; andre medlemmers navn og tall eksporteres ikke. |
| <img src="docs/icons/target.svg" width="56" height="56" alt="Mål"> | **Mål og ledelse** – måloppnåelse og målt aktivitet for dag, 7 og 30 dager. |
| <img src="docs/icons/privacy.svg" width="56" height="56" alt="Personvern"> | **Personvern** – avgrenset lesetilgang, uten GPS og personnavn. |

**Oversikten viser funksjoner under utvikling, ikke en ferdig installasjon.**

## ![Nøkkel](docs/icons/key.svg) Oppsett i betaen

1. Åpne **Grupper og deling → Home Assistant** i Tur-appen.
2. Velg hvilke data du tillater, og opprett en egen delingsnøkkel.
3. Lim nøkkelen inn i Tur-integrasjonens oppsett i Home Assistant.

**Dette er oppsettet som implementeres, ikke en installasjonsveiledning for en ferdig utgave.** Appens nye oppsettside og HA-klienten er ikke ferdige. Ingen MQTT-adresse eller MQTT-innlogging inngår i dette oppsettet.

## Data i denne betaens omfang

| Data | Betydning |
|---|---|
| Skritt | Dagens egne skritt |
| Distanse | Dagens aktivitetsdistanse i km |
| Aktivitetstid | Dagens trenings-/aktivitetsminutter |
| Høydemeter | Dagens stigning |
| Aktivitetspoeng | Dagens beregnede aktivitetspoeng |
| Måloppnåelse | Oppnådd andel av eget mål, når et mål er satt |
| Sist oppdatert | Tidspunktet tallene gjelder for |
| Egen lederstatus | Frivillig tilvalg, beskrevet under |

## ![Mål](docs/icons/target.svg) Lederstatus

Arbeidet omfatter egen status per gruppe for **i dag, siste 7 og siste 30 dager**, med **skritt, distanse, høyde, grunnpoeng og totalpoeng** som i appens grafer. Måloppnåelse og målt aktivitet beregnes separat.

Status er **leder**, **delt ledelse**, **leder ikke** eller **ukjent**. Manglende eller gamle sammenligningsdata gir ukjent. Ingen andre medlemmers navn eller aktivitetstall følger med.

Beregningsmodulen er kodet lokalt og passerer ti tester. Tilkoblingen til delingsvalget og HA-sensorene er ikke ferdig.

## ![Personvern](docs/icons/privacy.svg) Tilgang og personvern

- Egen nøkkel med bare lesetilgang til valgte tall. Den er separat fra vanlig appinnlogging.
- Oppretting, endring og tilbakekalling styres fra appkontoen.
- Serveren lagrer en kontrollverdi av nøkkelen og kontrollerer tillatelse ved hver lesing.
- Tilbakekalling stanser nye lesinger; allerede lagrede data hos mottakeren slettes ikke automatisk.
- GPS-ruter, posisjon, personnavn og andre medlemmers aktivitetstall inngår ikke.
- Gamle eller manglende data skal ikke fremstå som ferske nullverdier.
- App- og serverkode holdes privat. Dette repoet er for HA-integrasjonen og dokumentasjon.

## Status og testing

| Del | Bekreftet status |
|---|---|
| Serverens nøkkeltilgang | Kodet lokalt; ti nye tilgangstester passerer |
| Eksisterende serverfunksjoner | Alle 205 serverkontroller passerte før ledermodulen ble lagt til |
| Lederberegning | Ti nye beregningstester passerer |
| Android-oppsett og HA-klient | Ikke ferdig |
| Ferdig APK/serverpakke for denne utgaven | Ikke bygget |
| Ende-til-ende-test og fysisk telefon | Ikke utført |

## Testkrav for lederstatus

- Entydig førsteplass, delt førsteplass og at andre har høyere resultat.
- Manglende, gamle eller utilstrekkelige data gir ukjent.
- Riktige lokale datogrenser for i dag, siste 7 og siste 30 dager.
- Uavhengige grupper, målinger og sammenligningsmåter.
- Avslått eller tilbakekalt lederdeling gir ingen eksport av lederstatus.

Beregningsdelen er testet lokalt. Tester av delingsvalget og hele overføringen til Home Assistant gjenstår.

Dette er hoveddokumentet for aktivt arbeid i inneværende beta. Inaktive fremtidsideer er ikke med.

Ikke legg persondata, nøkler eller logger med hemmeligheter i offentlige feilrapporter.
