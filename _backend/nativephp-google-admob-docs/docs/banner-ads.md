# Banner Ads

Plugin supports anchored adaptive banner ads for top or bottom placement.

## Typical usage

```php
<?php

use lrakauskas\NativephpGoogleAdmob\Enums\BannerPosition;
use lrakauskas\NativephpGoogleAdmob\Facades\AdMobBanner;

# If you don't pass AdUnit ID, it falls back to value from config
AdMobBanner::showBanner(position: BannerPosition::Bottom);
AdMobBanner::getBannerStatus();
AdMobBanner::hideBanner();
```

or via JS bridge:

```js
import { On } from "#nativephp";
import {
  Events as AdMobEvents,
  googleAdmobBanner,
} from "#lrakauskas/nativephp-google-admob";

On(AdMobEvents.BannerShown, (payload) => {
  console.log("Banner shown!", payload);
});

await googleAdmobBanner.showBanner().position("bottom");
await googleAdmobBanner.getBannerStatus();
await googleAdmobBanner.hideBanner();
```

## Show Banner on App Start

Banners require some native components to be mounted and obviously you need to keep in mind that PHP side of your app will keep booting fresh on every request. Therefore, it's best to show banner on a landing page's controller. You should always check if the banner is already visible before showing it to avoid unnecessary API calls

```php
<?php

use lrakauskas\NativephpGoogleAdmob\Enums\BannerPosition;
use lrakauskas\NativephpGoogleAdmob\Facades\AdMobBanner;

class MyController extends Controller
{
    public function index()
    {
        if(! AdMobBanner::isBannerVisible()) {
            AdMobBanner::showBanner(position: BannerPosition::Bottom);
        }
    }

}
```

## Notes

- Banner ads can be shown at either the top or bottom of the screen
- Only one banner can be shown at a time. Showing a new banner replaces the existing one.
- Status calls let you inspect visibility and current native state
- Test mode swaps in Google demo ad units automatically
