# Tur Home Assistant

[English](README.md) | [Norsk](README.nb.md)

> **BETA – under development. This is an early test version, not a thoroughly tested product. Expect bugs and changes.**
>
> **This repository currently contains documentation only. The integration is not ready to install.**

The integration will retrieve your own approved activity data from the Tur server into Home Assistant. Planned setup: create a dedicated sharing key in the Tur app and paste it into Home Assistant.

## Planned for the first beta

- Today's steps, activity distance, activity time, elevation gain, activity points, goal achievement when a goal is set, and the last data update time.
- Read-only access to your own approved figures. The key will be revocable from the app.
- Transport is excluded from activity totals. GPS, groups and other people's activity are out of scope.
- Norwegian and English interfaces in a single integration.
- MQTT is deferred and is not included in this beta.

## Privacy

This public repository will contain only the Home Assistant integration, documentation and fictional examples. App and server source code, personal data, GPS tracks, production logs, databases, passwords and keys must remain private.

## Installation and testing

Installation instructions and test results will follow when the integration code is ready. No end-to-end or physical phone testing of this integration has been completed yet. Each release will state its beta status and known limitations.
