# Interstitial Ads

Interstitial ads use an explicit two-step lifecycle: load first, then show when ready.

## Typical usage

```php
use lrakauskas\NativephpGoogleAdmob\Facades\AdMobInterstitial;

AdMobInterstitial::loadInterstitial();

if (AdMobInterstitial::isInterstitialReady()) {
    AdMobInterstitial::showInterstitial();
}
```

## Recommended flow

1. Start loading before the moment you want to display the ad.
2. Check readiness if your UI depends on show success.
3. Listen to events for load failure, show failure, impression, click, and dismiss states.
