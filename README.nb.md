# Tur Home Assistant

[Norsk](README.nb.md) | [English](README.md)

> **BETA – under utvikling. Dette er en tidlig testutgave, ikke et gjennomtestet produkt. Feil og endringer må forventes.**
>
> **Foreløpig inneholder repoet bare dokumentasjon. Integrasjonen er ikke klar til installasjon.**

Integrasjonen skal hente dine egne, godkjente aktivitetstall fra Tur-serveren til Home Assistant. Planlagt oppsett: opprett en egen delingsnøkkel i Tur-appen og lim den inn i Home Assistant.

## Planlagt i første beta

- Dagens skritt, aktivitetsdistanse, aktivitetstid, høydemeter, aktivitetspoeng, måloppnåelse dersom mål er satt, og tidspunkt for siste oppdatering.
- Énveis lesetilgang til egne godkjente tall. Nøkkelen skal kunne trekkes tilbake fra appen.
- Transport holdes utenfor aktivitetstallene. GPS, grupper og andres aktivitet inngår ikke.
- Norsk og engelsk brukergrensesnitt i én integrasjon.
- MQTT utsettes og inngår ikke i denne betaen.

## Personvern

Dette offentlige repoet skal bare inneholde Home Assistant-integrasjonen, dokumentasjon og oppdiktede eksempler. App- og serverkode, brukerdata, GPS-spor, produksjonslogger, databaser, passord og nøkler skal holdes privat.

## Installasjon og testing

Installasjonsveiledning og testresultater kommer når integrasjonskoden er klar. Ingen ende-til-ende-test eller fysisk telefontest av denne integrasjonen er gjennomført ennå. Beta-status og kjente begrensninger skal oppgis i hver utgivelse.
