# Events

This page documents all public events emitted by the NativePHP Google AdMob plugin.

Use these events to react to ad lifecycle changes in your app.

## Event Overview

The table below is generated from the release artifact and refreshed on every plugin tag.

<!-- GENERATED:events_table:start -->
| Event | Description | Trigger |
| --- | --- | --- |
| `BannerHidden` | The banner ad was hidden. | When the currently visible banner ad is removed from view. |
| `BannerLoadFailed` | The banner ad failed to load. | When the native layer reports a load failure for the banner ad. |
| `BannerShown` | The banner ad is now visible to the user. | When the native layer confirms that the banner ad was shown. |
| `BannerStatusReceived` | Dispatches the latest native banner ad status snapshot. | After requesting banner ad status from the native layer. |
| `InterstitialClicked` | The interstitial ad was clicked. | When the ad SDK reports a click for the interstitial ad. |
| `InterstitialDismissed` | The interstitial ad was dismissed by the user. | When the full-screen interstitial ad is closed. |
| `InterstitialImpression` | The interstitial ad recorded an impression. | When the ad SDK reports an impression for the interstitial ad. |
| `InterstitialLoadFailed` | The interstitial ad failed to load. | When the native layer reports a load failure for the interstitial ad. |
| `InterstitialLoadRequested` | A load request for the interstitial ad has been sent to native code. | Immediately after calling the public load method for the interstitial ad. |
| `InterstitialLoaded` | The interstitial ad finished loading. | When the native layer reports that the interstitial ad is available. |
| `InterstitialShowFailed` | The interstitial ad failed to show. | When a native show attempt for the interstitial ad is rejected or errors. |
| `InterstitialShowRequested` | A show request for the interstitial ad has been sent to native code. | Immediately after calling the public show method for the interstitial ad. |
| `InterstitialShown` | The interstitial ad is now visible to the user. | When the native layer confirms that the interstitial ad was shown. |
| `InterstitialStatusReceived` | Dispatches the latest native interstitial ad status snapshot. | After requesting interstitial ad status from the native layer. |
| `RewardedClicked` | The rewarded ad was clicked. | When the ad SDK reports a click for the rewarded ad. |
| `RewardedDismissed` | The rewarded ad was dismissed by the user. | When the full-screen rewarded ad is closed. |
| `RewardedEarned` | The user earned the configured reward. | When a rewarded ad grants a reward to the user. |
| `RewardedImpression` | The rewarded ad recorded an impression. | When the ad SDK reports an impression for the rewarded ad. |
| `RewardedLoadFailed` | The rewarded ad failed to load. | When the native layer reports a load failure for the rewarded ad. |
| `RewardedLoadRequested` | A load request for the rewarded ad has been sent to native code. | Immediately after calling the public load method for the rewarded ad. |
| `RewardedLoaded` | The rewarded ad finished loading. | When the native layer reports that the rewarded ad is available. |
| `RewardedShowFailed` | The rewarded ad failed to show. | When a native show attempt for the rewarded ad is rejected or errors. |
| `RewardedShowRequested` | A show request for the rewarded ad has been sent to native code. | Immediately after calling the public show method for the rewarded ad. |
| `RewardedShown` | The rewarded ad is now visible to the user. | When the native layer confirms that the rewarded ad was shown. |
| `RewardedStatusReceived` | Dispatches the latest native rewarded ad status snapshot. | After requesting rewarded ad status from the native layer. |
<!-- GENERATED:events_table:end -->

## Payload Reference

Payload fields are generated from the artifact and should be treated as the source of truth for public event data.

<!-- GENERATED:events_payloads:start -->
### `BannerHidden`

The banner ad was hidden.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `BannerLoadFailed`

The banner ad failed to load.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `message` | `string` | yes | - | Native error or status message. |
| `code` | `?int` | no | null | Native or SDK error code when available. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `BannerShown`

The banner ad is now visible to the user.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `position` | `string` | yes | - | Banner position value reported by the native layer. |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null | Bridge correlation identifier when one is available. |
| `bannerHeightPx` | `int` | no | 0, | Measured banner height in pixels. |

### `BannerStatusReceived`

Dispatches the latest native banner ad status snapshot.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `visible` | `bool` | yes | - | Whether the banner is currently visible. |
| `position` | `string` | yes | - | Banner position value reported by the native layer. |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `sdkInitialized` | `bool` | yes | - | Whether the Google Mobile Ads SDK is initialized. |
| `platform` | `string` | no | android | Platform that emitted the event. |
| `id` | `?string` | no | null | Bridge correlation identifier when one is available. |
| `bannerHeightPx` | `int` | no | 0, | Measured banner height in pixels. |

### `InterstitialClicked`

The interstitial ad was clicked.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialDismissed`

The interstitial ad was dismissed by the user.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialImpression`

The interstitial ad recorded an impression.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialLoadFailed`

The interstitial ad failed to load.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `message` | `string` | yes | - | Native error or status message. |
| `code` | `?int` | no | null | Native or SDK error code when available. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialLoadRequested`

A load request for the interstitial ad has been sent to native code.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialLoaded`

The interstitial ad finished loading.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialShowFailed`

The interstitial ad failed to show.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `message` | `string` | yes | - | Native error or status message. |
| `code` | `?int` | no | null | Native or SDK error code when available. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialShowRequested`

A show request for the interstitial ad has been sent to native code.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `ready` | `bool` | yes | - | Whether the ad is ready to show. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialShown`

The interstitial ad is now visible to the user.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `InterstitialStatusReceived`

Dispatches the latest native interstitial ad status snapshot.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `ready` | `bool` | yes | - | Whether the ad is ready to show. |
| `loading` | `bool` | yes | - | Whether a load request is currently in progress. |
| `showing` | `bool` | yes | - | Whether the ad is currently being displayed. |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `sdkInitialized` | `bool` | yes | - | Whether the Google Mobile Ads SDK is initialized. |
| `platform` | `string` | no | android | Platform that emitted the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedClicked`

The rewarded ad was clicked.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedDismissed`

The rewarded ad was dismissed by the user.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedEarned`

The user earned the configured reward.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `amount` | `int` | yes | - | Reward amount granted to the user. |
| `type` | `string` | yes | - | Reward type or classification reported by AdMob. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedImpression`

The rewarded ad recorded an impression.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedLoadFailed`

The rewarded ad failed to load.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `message` | `string` | yes | - | Native error or status message. |
| `code` | `?int` | no | null | Native or SDK error code when available. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedLoadRequested`

A load request for the rewarded ad has been sent to native code.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedLoaded`

The rewarded ad finished loading.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedShowFailed`

The rewarded ad failed to show.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `message` | `string` | yes | - | Native error or status message. |
| `code` | `?int` | no | null | Native or SDK error code when available. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedShowRequested`

A show request for the rewarded ad has been sent to native code.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `ready` | `bool` | yes | - | Whether the ad is ready to show. |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedShown`

The rewarded ad is now visible to the user.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `adUnitId` | `?string` | no | null | AdMob ad unit ID associated with the event. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |

### `RewardedStatusReceived`

Dispatches the latest native rewarded ad status snapshot.

| Field | Type | Required | Default | Notes |
| --- | --- | --- | --- | --- |
| `ready` | `bool` | yes | - | Whether the ad is ready to show. |
| `loading` | `bool` | yes | - | Whether a load request is currently in progress. |
| `showing` | `bool` | yes | - | Whether the ad is currently being displayed. |
| `adUnitId` | `string` | yes | - | AdMob ad unit ID associated with the event. |
| `sdkInitialized` | `bool` | yes | - | Whether the Google Mobile Ads SDK is initialized. |
| `platform` | `string` | no | android | Platform that emitted the event. |
| `rewardAmount` | `int` | no | 0 | Latest reward amount reported by the native layer. |
| `rewardType` | `string` | no | - | Latest reward type reported by the native layer. |
| `id` | `?string` | no | null, | Bridge correlation identifier when one is available. |
<!-- GENERATED:events_payloads:end -->
