# API Reference: Config

These are the user-facing environment/config keys consumed by the plugin.

<!-- GENERATED:config_table:start -->
| Key | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `ADMOB_APP_ID` | `string` | Google test app id | yes (production) | Google AdMob application ID used by the Android integration. |
| `ADMOB_BANNER_ENABLED` | `bool` | false | no | Enables banner support in the generated Android integration. If you disable it after enabling it, run `php artisan native:install --force` again. |
| `ADMOB_BANNER_AD_UNIT_ID` | `string` | empty | yes (production banners) | Production ad unit ID for anchored adaptive banners. |
| `ADMOB_INTERSTITIAL_AD_UNIT_ID` | `string` | empty | yes (production interstitial) | Production ad unit ID for interstitial ads. |
| `ADMOB_REWARDED_AD_UNIT_ID` | `string` | empty | yes (production rewarded) | Production ad unit ID for rewarded ads. |
| `ADMOB_TEST_MODE` | `bool` | true | no | Uses Google official demo ad unit IDs instead of production IDs when enabled. |
<!-- GENERATED:config_table:end -->
