# Banner Ads

Banner support is anchored adaptive and designed for top or bottom placement.

## Typical usage

```php
use lrakauskas\NativephpGoogleAdmob\Enums\BannerPosition;
use lrakauskas\NativephpGoogleAdmob\Facades\AdMobBanner;

AdMobBanner::showBanner(position: BannerPosition::Bottom);
AdMobBanner::getBannerStatus();
AdMobBanner::hideBanner();
```

## Notes

- banner ads can be shown at the top or bottom of the screen
- status calls let you inspect visibility and current native state
- test mode swaps in Google demo ad units automatically
