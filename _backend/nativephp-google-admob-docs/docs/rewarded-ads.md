# Rewarded Ads

Rewarded ads use an explicit two-step lifecycle: you have to load first, then show when ready. In general, you want to load the ad as soon as possible and keep it ready for when you actually need it. When time is right to show, check if the ad is ready and show it. Listen to events to track the full lifecycle. You can only have one rewarded ad loaded at a time.

## Typical usage

```php
use lrakauskas\NativephpGoogleAdmob\Facades\AdMobRewarded;

AdMobRewarded::loadRewarded();

if (AdMobRewarded::isRewardedReady()) {
    AdMobRewarded::showRewarded();
}
```

or via JS bridge:

```js
import { On } from "#nativephp";
import { Events as AdMobEvents, googleAdmobRewarded } from "#lrakauskas/nativephp-google-admob";

On(AdMobEvents.RewardedLoaded, (payload) => {
  console.log("Rewarded loaded! Let's show it.", payload);
  await googleAdmobRewarded.showRewarded();
});

On(AdMobEvents.RewardedEarned, (payload) => {
  console.log("User earned reward!", payload);
  // Grant user the reward they deserved!
});

await googleAdmobRewarded.loadRewarded();
```

## Recommended flow

1. Load before the reward opportunity is presented.
2. Show only when the ad is ready.
3. Grant rewards based on the rewarded event payload rather than UI assumptions. Check `payload.amount` and `payload.type` to know what the user earned (you set these up in AdMob dashboard).
