# Configuration

AdUnit IDs are automatically resolved by PHP facades based on your config and test mode settings. When using JS bridge, you must always pass AdUnit ID manually and resolve test / production AdUnit IDs yourself.

## PHP

AdUnit ID is resolved in the following order:

- If test mode is enabled in config, it uses internal test AdUnit ID regardless of what you pass in method calls.
- If AdUnit ID is passed in method call, it uses that.
- If AdUnit ID is not passed in method call, it uses production AdUnit ID from your `.env` file. For example, `ADMOB_BANNER_AD_UNIT_ID`, `ADMOB_INTERSTITIAL_AD_UNIT_ID`, `ADMOB_REWARDED_AD_UNIT_ID`, etc.

## JS bridge

When using JS bridge, you must always pass AdUnit ID manually and resolve test / production AdUnit IDs yourself as you are effectively bypassing plugin's PHP side of AdUnit ID resolution. For example:

```js
import { On } from "#nativephp";
import { Events as AdMobEvents, googleAdmobInterstitial } from "#lrakauskas/nativephp-google-admob";

On(AdMobEvents.InterstitialLoaded, (payload) => {
  console.log("Interstitial loaded! Let's show it.", payload);
  await googleAdmobInterstitial.showInterstitial();
});

// We must always pass AdUnit ID when using JS bridge
await googleAdmobInterstitial.loadInterstitial().adUnitId("ca-app-pub-3940256099942544/1033173712");
```
