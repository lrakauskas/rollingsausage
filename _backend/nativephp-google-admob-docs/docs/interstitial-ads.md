# Interstitial Ads

Interstitial ads use an explicit two-step lifecycle: you have to load first, then show when ready. In general, you want to load the ad as soon as possible and keep it ready for when you actually need it. When time is right to show, check if the ad is ready and show it. Listen to events to track the full lifecycle. You can only have one interstitial ad loaded at a time.

## Typical usage

```php
<?php

use lrakauskas\NativephpGoogleAdmob\Facades\AdMobInterstitial;

AdMobInterstitial::loadInterstitial();

# At some later point when you want to show the ad
if (AdMobInterstitial::isInterstitialReady()) {
    AdMobInterstitial::showInterstitial();
}
```

or via JS bridge:

```js
import { On } from "#nativephp";
import { Events as AdMobEvents, googleAdmobInterstitial } from "#lrakauskas/nativephp-google-admob";

On(AdMobEvents.InterstitialLoaded, (payload) => {
  console.log("Interstitial loaded! Let's show it.", payload);
  await googleAdmobInterstitial.showInterstitial();
});

await googleAdmobInterstitial.loadInterstitial();
```

## Recommended flow

1. Start loading before the moment you want to display the ad.
2. Check readiness if your UI depends on show success.
3. Listen to events for load failure, show failure, impression, click, and dismiss states.
