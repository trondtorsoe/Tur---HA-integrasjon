# Tur Home Assistant

**Status: Under utvikling. Dette repoet inneholder foreløpig prosjektstruktur og krav, ikke en installerbar integrasjon.**

Integrasjonen skal hente brukerens egne aktivitetstall fra Tur-serveren til Home Assistant. Planlagt oppsett: opprett en egen delingsnøkkel i Tur-appen og lim den inn i integrasjonens oppsett i Home Assistant.

## Planlagt funksjonalitet

- Énveis lesing av egne aktivitetstall.
- Skritt, distanse, aktivitetstid, høydemeter, poeng, måloppnåelse og tidspunkt for siste oppdatering, avhengig av hva brukeren har godkjent.
- Transport skal ikke gi aktivitetskreditt.
- Ingen krav om MQTT-oppsett for denne integrasjonen. Generell MQTT-deling er et separat alternativ.
- Tilgang skal kunne trekkes tilbake i Tur-appen.
- Gamle målinger skal kunne skilles fra ferske målinger.

## Personvern og publisering

Dette repoet skal bare inneholde Home Assistant-integrasjonen, dokumentasjon og oppdiktede eksempeldata. App- og serverkode, brukerdata, GPS-spor, logger fra produksjon, databaser og hemmeligheter skal holdes utenfor.

GPS inngår ikke i første integrasjon. Eventuell senere støtte krever et eget uttrykkelig samtykke.

## Struktur

- `custom_components/tur/`: reservert for integrasjonskoden.
- `docs/design.md`: krav til dataflyt og nøkkeltilgang.

Distribusjonsformat og installasjonsveiledning fastsettes etter kontroll mot gjeldende Home Assistant-dokumentasjon og testing av integrasjonen.
