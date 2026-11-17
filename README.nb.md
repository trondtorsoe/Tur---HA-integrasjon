# Tur for Home Assistant — Beta

[English](README.md) | [Norsk](README.nb.md)

> **BETA — under utvikling, ikke et gjennomtestet produkt. Krever Tur Android 0.20 B8 og server oppdatert med B8-pakken.**

Vis egne godkjente aktivitetstall og lederstatus fra Tur i Home Assistant. Integrasjonen leser via Tur-serveren; du trenger ikke åpne hjemmenettet for inngående trafikk.

| Appikon | Funksjon |
|---|---|
| <img src="docs/icons/key.svg" width="56" height="56" alt="Nøkkel"> | Opprett, kopier, erstatt eller trekk tilbake egen delingsnøkkel. |
| <img src="docs/icons/sharing.svg" width="56" height="56" alt="Deling"> | Velg hvilke av dine egne tall som kan leses. |
| <img src="docs/icons/groups.svg" width="56" height="56" alt="Grupper"> | Valgfri egen lederstatus, uten andres navn og tall. |
| <img src="docs/icons/target.svg" width="56" height="56" alt="Mål"> | Måloppnåelse og målt aktivitet sammenlignes hver for seg. |
| <img src="docs/icons/privacy.svg" width="56" height="56" alt="Personvern"> | Kun lesetilgang; ingen GPS, posisjon eller personnavn. |

## Kom i gang

1. Oppdater Tur-serveren med B8-pakken, og installer **Tur 0.20 B8** over eksisterende Android-app. Ikke avinstaller først.
2. Åpne **Grupper og deling → Home Assistant** i Tur. Appen spør ved behov om oppretting/tilkobling av Tur-konto; ingen gruppe er nødvendig.
3. Velg tall og trykk **Opprett nøkkel**. Kopier nøkkelen og behandle den som et passord.
4. Under [egendefinerte repoer i HACS](https://hacs.dev/docs/faq/custom_repositories/) legger du til `https://github.com/trondtorsoe/Tur---HA-integrasjon`, kategori **Integration**. Last ned **Tur Home Assistant (Beta)** og start Home Assistant på nytt.
5. Velg **Innstillinger → Enheter og tjenester → Legg til integrasjon → Tur**, og lim inn nøkkelen.

Krever **Home Assistant 2026.11.0 eller nyere**. Alternativt kopierer du bare `custom_components/tur_activity` fra repoet til Home Assistants `config/custom_components/` og starter på nytt. Dette er en egendefinert integrasjon, ikke en integrasjon inkludert i Home Assistant Core eller standardlisten i HACS.

## Tall og oppdatering

| Sensor | Betydning |
|---|---|
| Skritt | Dine skritt i dag |
| Aktivitetsdistanse | Dagens aktivitetsdistanse i km |
| Aktivitetstid | Dagens registrerte trenings-/aktivitetsminutter |
| Høydemeter | Dagens kjente stigning i meter |
| Totalpoeng | Dagens beregnede totalpoeng |
| Måloppnåelse | Oppnåelse av eget dagsmål, begrenset til 100 %, hvis satt |
| Sist oppdatert | Tidspunktet aktivitetstallene gjelder |

Appen sender ved vanlig synkronisering. **Send tall nå** finnes også på Home Assistant-siden. Home Assistant leser omtrent hvert femte minutt. Transport gir ikke aktivitetskreditt. Oppsett og sensornavn støtter norsk og engelsk; Home Assistant følger eget språkvalg.

Tall som ikke er valgt, mangler, gjelder en tidligere dag eller er over seks timer gamle, blir **utilgjengelige**, ikke ferske nuller. Sist oppdatert vises fortsatt når tidspunktet finnes. Androids bakgrunnsbegrensninger og nettforbindelse kan forsinke sendingen.

## Lederstatus

Aktiver **Min lederstatus per gruppe** som eget valg i Tur. Sensorene dekker **i dag, siste 7 dager og siste 30 dager**, for **skritt, distanse, høyde, grunnpoeng og totalpoeng**. Målt aktivitet summeres for perioden; måloppnåelse sammenligner snitt av dagsprosentene, separat fra målt aktivitet.

Status er **leder**, **delt ledelse**, **leder ikke** eller **ukjent / utilstrekkelige data**. Gamle eller manglende sammenligningstall gir ukjent. Medlemmer uten personlige mål utelates fra målsammenligningen; mangler du selv mål, blir din målstatus ukjent.

Bare din status eksporteres. Grupper vises med tekniske identifikatorer i sensornavnene, uten gruppe- og personnavn; gi sensorene egne navn i Home Assistant om ønskelig. En gruppe kan opprette inntil 30 ledersensorer. Fjernede grupper eller trukket lederdeling gjør de tilhørende sensorene utilgjengelige.

## Nøkler og personvern

- Nøkkelen gir bare lesetilgang til valgte tall, separat fra vanlig innlogging i appen.
- Serveren lagrer en kontrollverdi av nøkkelen og sjekker tillatelsen ved hver lesing.
- Endre valg eller trekk tilbake tilgangen på appens Home Assistant-side. Endringer gjelder fra neste forespørsel.
- En ny nøkkel gjør den gamle ugyldig umiddelbart. Bruk **Konfigurer på nytt** på eksisterende integrasjon for å lime inn ny nøkkel; innloggingsfeil tilbyr også ny godkjenning.
- Allerede lagrede tall i Home Assistant slettes ikke automatisk ved tilbakekall.
- Nøkler sendes i HTTPS-autorisasjonshodet, aldri i nettadressen. Ikke legg nøkler, GPS-spor eller personlige logger i offentlige feilrapporter.
- Android- og serverkildekode er privat. Bare kildekoden til Home Assistant-integrasjonen publiseres her.

## Kontroller og begrensninger

B8 består **216 servertester**, **14 database-/menytester**, **20 Android-regresjonssuiter** og **tre tester av nettvisningene**. Sju integrasjonstester kjører mot **ekte Home Assistant 2026.11**, lokal HTTPS-server og Tur-serverkoden. De dekker oppsett og sensorer, egen lederstatus, manglende/gamle tall, endrede delingsvalg, nøkkelbytte/tilbakekall, ugyldige svar og videresendinger. APK-signatur og filjustering er kontrollert.

Dette er automatiske kontroller. Installasjon på en testers fysiske telefon og Home Assistant-installasjon gjenstår å kontrollere. VPS-en må oppdateres med B8-pakken før det nye endepunktet kan brukes. Stabile 0.20-brukere tvinges ikke til å oppdatere for denne integrasjonen.

Se også [Tur for Android](https://github.com/trondtorsoe/Tur-Activity-Tracker-for-Android).
