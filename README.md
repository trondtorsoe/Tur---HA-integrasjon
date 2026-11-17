# Tur for Home Assistant — Beta

[English](README.md) | [Norsk](README.nb.md)

> **BETA — active development, not a thoroughly tested product. Requires Tur Android 0.20 B8 and a server updated with the B8 package.**

Show your own approved Tur activity figures and leadership status in Home Assistant. The integration reads through the Tur server; no inbound connection to your home network is needed.

| App icon | Feature |
|---|---|
| <img src="docs/icons/key.svg" width="56" height="56" alt="Key"> | Create, copy, replace or revoke a dedicated sharing key. |
| <img src="docs/icons/sharing.svg" width="56" height="56" alt="Sharing"> | Choose which of your own figures may be read. |
| <img src="docs/icons/groups.svg" width="56" height="56" alt="Groups"> | Optional own leadership status, without other members' names or figures. |
| <img src="docs/icons/target.svg" width="56" height="56" alt="Goals"> | Goal achievement and measured activity are separate comparisons. |
| <img src="docs/icons/privacy.svg" width="56" height="56" alt="Privacy"> | Read-only access; no GPS, location or personal names. |

## Setup

1. Update the Tur server with the B8 package, then install **Tur 0.20 B8** over your existing Android app. Do not uninstall first.
2. In Tur, open **Groups and sharing → Home Assistant**. If needed, the app asks you to create/connect your Tur account; no group is required.
3. Select your figures and press **Create key**. Copy the key and treat it as a password.
4. In [HACS custom repositories](https://hacs.dev/docs/faq/custom_repositories/), add `https://github.com/trondtorsoe/Tur---HA-integrasjon` with category **Integration**. Download **Tur Home Assistant (Beta)** and restart Home Assistant.
5. Open **Settings → Devices & services → Add integration → Tur**, then paste the key.

Requires **Home Assistant 2026.11.0 or newer**. Alternatively, copy only `custom_components/tur_activity` from this repository to your Home Assistant `config/custom_components/` directory, then restart. The integration is a custom component, not an integration included in Home Assistant Core or a default HACS listing.

## Figures and update behaviour

| Sensor | Meaning |
|---|---|
| Steps | Your steps today |
| Activity distance | Today's activity distance in km |
| Activity time | Today's recorded training/activity minutes |
| Elevation gain | Today's known ascent in metres |
| Total points | Today's calculated total points |
| Goal achievement | Progress towards your daily goal, capped at 100%, if set |
| Last updated | Time the activity snapshot refers to |

The app sends a snapshot during normal synchronisation; **Send figures now** is also available on its Home Assistant page. Home Assistant reads approximately every five minutes. Transport is excluded from activity credit. The setup and sensor names support English and Norwegian; Home Assistant selects its own language.

Unselected, missing, previous-day or more than six-hour-old activity data becomes **unavailable**, not a fresh zero. Last updated remains visible when available. Android background and network restrictions can delay uploads.

## Leadership status

Enable **My leadership status per group** separately in Tur. Sensors cover **today, the last 7 days and the last 30 days**, for **steps, distance, elevation, base points and total points**. Measured activity sums the period; goal achievement compares the average daily percentages, separately from measured activity.

The states are **leading**, **tied lead**, **not leading** and **unknown / insufficient data**. Stale or missing competitor data gives unknown. Members without personal goals are excluded from the goal comparison; your own missing goal gives unknown.

Only your status is exported. Groups use opaque identifiers in sensor names, not group or member names; rename the entities in Home Assistant if useful. One participating group can create up to 30 leadership sensors. Removed groups or withdrawn leadership permission make the associated sensors unavailable.

## Keys and privacy

- The key grants read-only access to selected figures, separate from normal app login.
- The server stores a hash of the key; permissions are checked on every request.
- Change sharing choices or revoke access on the app's Home Assistant page. Changes apply on the next request.
- A replacement key immediately invalidates the old key. Use **Reconfigure** on the existing integration to paste the replacement; authentication failures also offer reauthentication.
- Data already saved in Home Assistant is not automatically deleted when access is revoked.
- Keys are sent in the HTTPS authorization header, never in a URL. Do not post keys, GPS tracks or personal logs in public issues.
- Android app and server source remain private. Only the Home Assistant integration source is published here.

## Verification and limitations

B8 passes **216 server tests**, **14 database/menu tests**, **20 Android Java regression suites** and **three web rendering suites**. Seven integration tests run against **actual Home Assistant 2026.11**, a local HTTPS server and the Tur server implementation. They cover setup and sensors, own leadership, missing/stale data, scope changes, key replacement/revocation, malformed responses and redirects. APK signing and alignment are verified.

These are automated checks. Installation on a tester's physical phone and their Home Assistant installation still needs verification. The VPS must receive the B8 package before the new endpoint can be used. Existing stable 0.20 users are not forced to update for this integration.

See also [Tur for Android](https://github.com/trondtorsoe/Tur-Activity-Tracker-for-Android).
