# Neste beta / Next beta

**BETA — aktivt utviklingsarbeid, ikke en ferdig eller gjennomtestet utgivelse.**  
**BETA — active development, not a finished or thoroughly tested release.**

Bare arbeid som inngår i neste beta beskrives her. / Only work actively included in the next beta is described here.

## ![Nøkkel / Key](icons/key.svg) Nøkkelbasert deling / Key-based sharing

**Norsk:** Egen HA-nøkkel med lesetilgang til brukerens godkjente aktivitetstall. Serverkoden er implementert lokalt, men er ikke satt i produksjon. Appoppsett, HA-klient og full integrasjonstest er ikke ferdige. De ti nye tilgangstestene og alle 205 serverkontroller passerer lokalt.

**English:** A dedicated HA key grants read-only access to the user's approved activity figures. Server code is implemented locally but has not been deployed. App setup, the HA client and full integration testing are incomplete. Ten new access tests and all 205 server checks pass locally.

## ![Mål / Goals](icons/target.svg) Egen lederstatus / Personal leadership status

**Status: spesifisert, ikke implementert eller testet. / Specified, not implemented or tested.**

**Norsk**
- Eget frivillig delingsvalg.
- Egen status per gruppe og aktivitetstype, for i dag, siste 7 dager og siste 30 dager.
- Måloppnåelse og målt aktivitet holdes adskilt.
- Mulige verdier: leder, delt ledelse, leder ikke, ukjent.
- Manglende eller utilstrekkelige sammenligningsdata gir ukjent.
- Beregningstidspunkt følger med. Ingen navn eller aktivitetstall fra andre medlemmer eksporteres.
- Koblingen til appens eksisterende sammenligningsregler må kontrolleres før funksjonen regnes som klar.

**English**
- A separate opt-in sharing choice.
- The user's own status per group and activity type, for today, the last 7 days and the last 30 days.
- Goal achievement and measured activity remain separate.
- States: leading, tied lead, not leading, unknown.
- Missing or insufficient comparison data gives unknown.
- Includes calculation time. Other members' names and activity figures are not exported.
- Alignment with the app's existing comparison rules must be verified before this feature is considered ready.

### Testkrav / Acceptance checks

1. Entydig førsteplass / Unique first place.
2. Delt førsteplass / Tied first place.
3. Andre har høyere resultat / Another member has a higher result.
4. Manglende, gamle eller utilstrekkelige data / Missing, stale or insufficient data.
5. Riktige datogrenser for dag, 7 og 30 dager i brukerens tidssone / Correct local boundaries for today, 7 and 30 days.
6. Uavhengige grupper, aktivitetstyper og sammenligningsmåter / Independent groups, activity types and comparison modes.
7. Avslått eller tilbakekalt deling gir ingen eksport av lederstatus / Disabled or revoked sharing exports no leadership status.

## ![Personvern / Privacy](icons/privacy.svg) Personvern / Privacy

App- og serverkildekode, nøkler og brukerdata holdes privat. Bare HA-integrasjonskoden publiseres her når den er klar.  
App and server source code, keys and personal data remain private. Only the HA integration code is published here when ready.
