# Tur Home Assistant

[English](README.md) | [Norsk](README.nb.md)

> **BETA – active development. Not a thoroughly tested product. No installable integration has been published yet.**

The Tur integration is being developed to show your own approved activity figures in Home Assistant, alongside the next beta of [Tur for Android](https://github.com/trondtorsoe/Tur-Activity-Tracker-for-Android).

## ![Key](docs/icons/key.svg) Beta setup

1. Open **Groups and sharing → Home Assistant** in the Tur app.
2. Select the data you permit and create a dedicated sharing key.
3. Paste the key into the Tur integration setup in Home Assistant.

**This describes the setup being implemented, not instructions for an available release.** The app setup page and HA client are incomplete. This setup does not require an MQTT address or MQTT credentials.

## Data included in this beta's scope

| Data | Meaning |
|---|---|
| Steps | Your steps today |
| Distance | Today's activity distance in km |
| Activity time | Today's training/activity minutes |
| Elevation gain | Today's ascent |
| Activity points | Today's calculated activity points |
| Goal achievement | Progress towards your own goal, when set |
| Last updated | Time the figures refer to |
| Own leadership status | Separate opt-in, described below |

## ![Goals](docs/icons/target.svg) Leadership status

Active work covers your own status per group for **today, the last 7 days and the last 30 days**, for **steps, distance, elevation, base points and total points**, matching the app's charts. Goal achievement and measured activity are calculated separately.

States are **leading**, **tied lead**, **not leading** or **unknown**. Missing or stale comparison data gives unknown. Other members' names and activity figures are not exported.

The calculation module is implemented locally and passes ten tests. Connecting it to the sharing choice and HA sensors is incomplete.

## ![Privacy](docs/icons/privacy.svg) Access and privacy

- A dedicated key grants read-only access to selected figures, separate from normal app login.
- Creation, changes and revocation are controlled through the app account.
- The server stores a verification hash of the key and checks permissions on every read.
- Revocation stops new reads; data already saved by a recipient is not automatically deleted.
- GPS routes, location, personal names and other members' activity figures are excluded.
- Old or missing data must not appear as fresh zero measurements.
- App and server source code remain private. This repository is for the HA integration and documentation.

## Status and testing

| Component | Confirmed status |
|---|---|
| Server key access | Implemented locally; ten new access tests pass |
| Existing server features | All 205 server checks passed before the leadership module was added |
| Leadership calculation | Ten new calculation tests pass |
| Android setup and HA client | Incomplete |
| APK/server package for this release | Not built |
| End-to-end and physical phone testing | Not performed |

See [active next-beta work and acceptance checks](docs/next-beta.md). This documentation describes active work, not a finished release. Inactive future ideas are excluded.

Do not post personal data, keys or logs containing secrets in public issues.
