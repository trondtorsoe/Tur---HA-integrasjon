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
4. Åpne **Innstillinger → Markedsplass → Legg til fra lenke** (engelsk: **Settings → Marketplace → Add from link**). Lim inn `https://github.com/trondtorsoe/Tur---HA-integrasjon` og velg **Legg til**. Velg **Integrasjon** hvis du blir spurt. Markedsplassen veileder deg gjennom GitHub-tilkobling ved behov. Åpne **Tur Home Assistant (Beta)** og velg **Installer**. Følg eventuell beskjed om omstart.
5. Velg **Innstillinger → Enheter og tjenester → Legg til integrasjon → Tur**, og lim inn nøkkelen.

Krever **Home Assistant 2026.11.0 eller nyere**. Alternativt kopierer du bare `custom_components/tur_activity` fra repoet til Home Assistants `config/custom_components/` og starter på nytt. Markedsplassen er innebygd i Home Assistant 2026.11; du trenger ikke installere HACS separat. Tur legges foreløpig til fra repo-lenken og er ikke oppført i standardkatalogen. [Offisiell veiledning for Markedsplassen](https://www.home-assistant.io/integrations/marketplace/#custom-repositories).

## Versjon og ikon

Home Assistant-integrasjonen er fortsatt **beta**. Utgave **0.20.2b3** viser integrasjonens versjon under **Enhetsinformasjon → Programvare** og bruker Tur-appens ikon med føtter og stiplet linje. Dette er integrasjonens versjon, ikke Android-versjonen. Android B8 og eksisterende server kan beholdes.

Etter oppdatering eller ny nedlasting i Markedsplassen må Home Assistant startes på nytt for å laste ny kode. Last siden på nytt hvis nettleseren fortsatt viser gammelt ikon. Du trenger ikke slette integrasjonen, nøkkelen eller sensorene.

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

Fra **0.20.2b3** opprettes en ny aktivitetssensor først når en valgt, fersk verdi finnes. Målt null er gyldig; manglende verdi regnes ikke som null. Sensorer legges automatisk til når data kommer senere. Eksisterende sensorer blir **utilgjengelige** hvis tallene ikke lenger er valgt, mangler, gjelder en tidligere dag eller er over seks timer gamle. Entitets-ID, historikk og automasjoner beholdes. Sist oppdatert vises fortsatt når tidspunktet finnes. Androids bakgrunnsbegrensninger og nettforbindelse kan forsinke sendingen.

## Lederstatus

Aktiver **Min lederstatus per gruppe** som eget valg i Tur. Sensorene dekker **i dag, siste 7 dager og siste 30 dager**, for **skritt, distanse, høyde, grunnpoeng og totalpoeng**. Målt aktivitet summeres for perioden; måloppnåelse sammenligner snitt av dagsprosentene, separat fra målt aktivitet.

Status er **leder**, **delt ledelse** eller **leder ikke**. En ny ledersensor opprettes først når sammenligningen er kjent og fersk. Ukjente sammenligninger oppretter ingen tomme entiteter. Eksisterende sensorer beholdes og blir **utilgjengelige** når sammenligningen midlertidig ikke kan beregnes. Medlemmer uten personlige mål utelates fra målsammenligningen; mangler du selv mål, opprettes ikke den målsensoren. Manglende tall gjettes ikke.

Bare din status eksporteres. Gruppenavnet fra appen vises i sensornavnet; teknisk gruppe-ID er den faste identiteten. Andres personnavn og tall eksporteres ikke. En gruppe kan opprette inntil 30 ledersensorer. Fjernede grupper eller trukket lederdeling gjør de tilhørende sensorene utilgjengelige.

## Lesbare gruppenavn

Fra **0.20.2b2** brukes gruppenavn fra Tur automatisk, også ved navneendring, uten nye entiteter. Du kan fortsatt velge egne lokale gruppenavn under **Innstillinger → Enheter og tjenester → Tur → Alternativer/konfigurer** (tannhjulet ved integrasjonen). Velg teknisk gruppe-ID og skriv ønsket navn, for eksempel «Familien». Gjenta for andre grupper. Tomt lokalt navn bruker navnet fra appen (eller ID-en med eldre server). Navnet sendes ikke til Tur-serveren, og eksisterende sensor-ID-er og automasjoner beholdes.

Endringen i hvilke sensorer som opprettes, krever bare **0.20.2b3** av Home Assistant-integrasjonen, ingen ny app eller server. Automatiske gruppenavn krever B9-eksporten på serveren. Sammenligninger krever ferske tall for alle dagene i perioden, og måloppnåelse krever egne mål. Eksisterende registrerte entiteter beholdes. Ønsker du en ren entitetsliste, kan du fjerne og legge til integrasjonen etter oppdatering og omstart av Home Assistant. Ny oppretting kan endre entitets-ID-er som brukes i automasjoner.

## Nøkler og personvern

- Nøkkelen gir bare lesetilgang til valgte tall, separat fra vanlig innlogging i appen.
- Serveren lagrer en kontrollverdi av nøkkelen og sjekker tillatelsen ved hver lesing.
- Endre valg eller trekk tilbake tilgangen på appens Home Assistant-side. Endringer gjelder fra neste forespørsel.
- En ny nøkkel gjør den gamle ugyldig umiddelbart. Bruk **Konfigurer på nytt** på eksisterende integrasjon for å lime inn ny nøkkel; innloggingsfeil tilbyr også ny godkjenning.
- Allerede lagrede tall i Home Assistant slettes ikke automatisk ved tilbakekall.
- Nøkler sendes i HTTPS-autorisasjonshodet, aldri i nettadressen. Ikke legg nøkler, GPS-spor eller personlige logger i offentlige feilrapporter.
- Android- og serverkildekode er privat. Bare kildekoden til Home Assistant-integrasjonen publiseres her.

## Kontroller og begrensninger

B8 består **216 servertester**, **14 database-/menytester**, **20 Android-regresjonssuiter** og **tre tester av nettvisningene**. Elleve integrasjonstester kjører mot **ekte Home Assistant 2026.11**, lokal HTTPS-server og Tur-serverkoden. De dekker oppsett og sensorer, egen lederstatus, manglende/gamle tall, endrede delingsvalg, nøkkelbytte/tilbakekall, ugyldige svar og videresendinger. APK-signatur og filjustering ble kontrollert for B8. De nye integrasjonskontrollene dekker tom førstegangsinstallasjon, gyldige nuller kontra manglende verdier, senere sensoroppretting, delvis sammenligningshistorikk, uendrede ID-er ved navneendring og gjenoppretting av registrerte utilgjengelige sensorer ved ny lasting.

**Bekreftet i faktisk bruk 17.11.2026:** En tester mottar løpende tall fra sin Android-app via Tur-serveren til sin Home Assistant. Sensorlisten viser skritt, distanse, aktivitetstid, høyde, poeng, måloppnåelse og oppdateringstid. Dagens lederstatus mottas for flere målinger, med Leder, Leder ikke og Delt ledelse, og måloppnåelse vises separat fra målt aktivitet.

Også bekreftet i faktisk bruk: ikon og gruppenavn fra appen, nøkkelbytte, sperring av gammel nøkkel og separat tilbakekall. Samsvar med tallene i Tur, sammenligninger for 7/30 dager, endrede delingsvalg, automatisk sensoroppretting når manglende data kommer, bevaring av entiteter/historikk ved omstart eller navneendring og lokale gruppenavn er ikke manuelt bekreftet av testeren ennå. Automatiske kontroller av flere av disse funksjonene er omtalt ovenfor. Stabile 0.20-brukere tvinges ikke til å oppdatere.

Se også [Tur for Android](https://github.com/trondtorsoe/Tur-Activity-Tracker-for-Android).
