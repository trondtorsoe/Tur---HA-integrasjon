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
4. Open **Settings → Marketplace → Add from link**. Enter `https://github.com/trondtorsoe/Tur---HA-integrasjon` and select **Add**. If asked, choose **Integration**. The Marketplace guides you through connecting GitHub if required. Open **Tur Home Assistant (Beta)** and select **Install**. Follow any restart prompt.
5. Open **Settings → Devices & services → Add integration → Tur**, then paste the key.

Requires **Home Assistant 2026.11.0 or newer**. Alternatively, copy only `custom_components/tur_activity` from this repository to your Home Assistant `config/custom_components/` directory, then restart. The Marketplace is built into Home Assistant 2026.11; no separate HACS installation is needed. Tur is currently added from its repository link, not listed in the default catalog. [Official Marketplace instructions](https://www.home-assistant.io/integrations/marketplace/#custom-repositories).

## Version and icon

The Home Assistant integration remains **beta**. Version **0.20.2b3** displays the integration version under **Device info → Firmware** and ships Tur's footprints-and-dotted-line icon. This is the integration version, not the Android version. Android B8 and the existing server remain compatible.

After updating or downloading again through Marketplace, restart Home Assistant to load the new code. Refresh the page if your browser still shows the old icon. Do not delete the integration, key or sensors.

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

From **0.20.2b3**, a new activity sensor is created only after a selected, fresh, non-null value arrives. A genuine zero is valid. Sensors are added automatically on later updates, so there is no need to reinstall when new data becomes available. Existing sensors become **unavailable** when their data is unselected, missing, from a previous day or more than six hours old; they are retained to preserve entity IDs, history and automations. Last updated remains visible when available. Android background and network restrictions can delay uploads.

## Leadership status

Enable **My leadership status per group** separately in Tur. Sensors cover **today, the last 7 days and the last 30 days**, for **steps, distance, elevation, base points and total points**. Measured activity sums the period; goal achievement compares the average daily percentages, separately from measured activity.

The states are **leading**, **tied lead** and **not leading**. A new leadership sensor is created only when its comparison is known and fresh; unknown comparisons do not create placeholder entities. Existing sensors become **unavailable** while their comparison cannot be calculated. Members without personal goals are excluded from goal comparisons; your own missing goal prevents that comparison. No missing value is treated as zero.

Only your status is exported. Group names from the app are shown in sensor names; opaque group IDs remain the permanent identity. Other members’ names and figures are not exported. One participating group can create up to 30 leadership sensors. Removed groups or withdrawn leadership permission make the associated sensors unavailable.

## Readable group names

Integration **0.20.2b2** automatically uses group names from Tur and follows name changes without creating new entities. You can also set local group aliases under **Settings → Devices & services → Tur → Options/configure** (the integration's cog button). Select the technical group ID and enter a name such as “Family”. Repeat for other groups. An empty alias restores the name from the app (or the ID on older servers). Names are not sent to the Tur server. Existing sensor unique IDs and automations are preserved.

The new entity-creation behaviour requires only this Home Assistant integration update; no new Android app or server is required. Automatic app group names require the B9 server export. Comparisons require fresh data for every day of the period, and goal achievement requires your own goals. Existing registered entities are retained; for a clean entity list, remove and re-add the integration after updating its code and restarting Home Assistant. Re-adding can change entity IDs used by automations.

## Keys and privacy

- The key grants read-only access to selected figures, separate from normal app login.
- The server stores a hash of the key; permissions are checked on every request.
- Change sharing choices or revoke access on the app's Home Assistant page. Changes apply on the next request.
- A replacement key immediately invalidates the old key. Use **Reconfigure** on the existing integration to paste the replacement; authentication failures also offer reauthentication.
- Data already saved in Home Assistant is not automatically deleted when access is revoked.
- Keys are sent in the HTTPS authorization header, never in a URL. Do not post keys, GPS tracks or personal logs in public issues.
- Android app and server source remain private. Only the Home Assistant integration source is published here.

## Verification and limitations

B8 passes **216 server tests**, **14 database/menu tests**, **20 Android Java regression suites** and **three web rendering suites**. Eleven integration tests run against **actual Home Assistant 2026.11**, a local HTTPS server and the Tur server implementation. They cover setup and sensors, own leadership, missing/stale data, scope changes, key replacement/revocation, malformed responses and redirects. The b3 checks include empty first installation, valid zeros versus missing values, later sensor creation, partial comparison history, no duplicate IDs, group renames, and restoration of registered unavailable sensors on reload. APK signing and alignment are verified.

**Confirmed in real use on 17 November 2026:** A tester receives ongoing figures from their Android app through the Tur server into their Home Assistant. Their sensor list displays steps, distance, activity time, ascent, points, goal achievement and update time. Today's leadership is received for several metrics, including Leading, Not leading and Tied lead, separately for goal achievement and measured activity.

Also confirmed in real use: the icon and app group names, key replacement, rejection of the previous key, and explicit revocation. Agreement with Tur's figures, 7/30-day comparisons, sharing-choice changes, automatic creation when missing data arrives, entity/history preservation across restart or group rename, and local group aliases have not yet been manually confirmed by the tester. Automated checks for several of these are described above. Existing stable 0.20 users are not forced to update.

See also [Tur for Android](https://github.com/trondtorsoe/Tur-Activity-Tracker-for-Android).
