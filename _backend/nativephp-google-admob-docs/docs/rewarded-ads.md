# Rewarded Ads

Rewarded ads also use an explicit load then show flow, with reward metadata returned through events and status calls.

## Typical usage

```php
use lrakauskas\NativephpGoogleAdmob\Facades\AdMobRewarded;

AdMobRewarded::loadRewarded();

if (AdMobRewarded::isRewardedReady()) {
    AdMobRewarded::showRewarded();
}
```

## Recommended flow

1. Load before the reward opportunity is presented.
2. Show only when the ad is ready.
3. Grant rewards based on the rewarded event payload rather than UI assumptions.
