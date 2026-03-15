# API Reference: Facades

Facades are the public PHP entrypoint for the package.

<!-- GENERATED:facades_methods:start -->
## `AdMobBanner`

Banner ad controls for showing, hiding, and inspecting anchored adaptive banners.

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `showBanner` | `?string $adUnitId = null, BannerPosition $position = BannerPosition::Bottom` | `array{position: "top"|"bottom", adUnitId: string}|null` | Shows an anchored adaptive banner using either the configured banner unit ID or the Google test unit in test mode. |
| `hideBanner` | `none` | `array<string, mixed>|null` | Hides the currently visible banner. |
| `getBannerStatus` | `none` | `array{visible: bool, position: "top"|"bottom", adUnitId: string, sdkInitialized: bool, platform: string, bannerHeightPx: int}|null` | Returns the latest native banner state snapshot. |
| `isBannerVisible` | `none` | `bool` | Returns whether a banner is currently visible. |

## `AdMobInterstitial`

Interstitial ad lifecycle controls with explicit load-then-show flow.

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `loadInterstitial` | `?string $adUnitId = null` | `array{loading: bool, adUnitId: string}|null` | Starts loading an interstitial ad. |
| `showInterstitial` | `none` | `array{requested: bool, ready: bool}|null` | Attempts to show a previously loaded interstitial ad. |
| `getInterstitialStatus` | `none` | `array{ready: bool, loading: bool, showing: bool, adUnitId: string, sdkInitialized: bool, platform: string}|null` | Returns the latest native interstitial state snapshot. |
| `isInterstitialReady` | `none` | `bool` | Returns whether an interstitial ad is ready to show. |

## `AdMobRewarded`

Rewarded ad lifecycle controls with explicit load-then-show flow.

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `loadRewarded` | `?string $adUnitId = null` | `array{loading: bool, adUnitId: string}|null` | Starts loading a rewarded ad. |
| `showRewarded` | `none` | `array{requested: bool, ready: bool}|null` | Attempts to show a previously loaded rewarded ad. |
| `getRewardedStatus` | `none` | `array{ready: bool, loading: bool, showing: bool, adUnitId: string, sdkInitialized: bool, platform: string, rewardType: string, rewardAmount: int}|null` | Returns the latest native rewarded state snapshot. |
| `isRewardedReady` | `none` | `bool` | Returns whether a rewarded ad is ready to show. |
<!-- GENERATED:facades_methods:end -->

## Usage style

- use facade calls from your NativePHP application code
- prefer enum values over raw strings where enums are provided
- use status methods when your UI needs to inspect current native state
