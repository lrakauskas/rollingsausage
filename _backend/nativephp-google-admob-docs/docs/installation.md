# Installation

Plugin is distributed via [NativePHP's Plugin Marketplace](https://nativephp.com/plugins/marketplace). You can also install it directly from the package repository if you have access.

Install the package into your NativePHP app and register the plugin provider.

## 1. Add a path or private repository source

For local package development, add a path repository to your app `composer.json`:

```json
{
  "repositories": [
    {
      "type": "path",
      "url": "packages/nativephp-google-admob",
      "options": {
        "symlink": true
      }
    }
  ]
}
```

For premium package installs from NativePHP, use the repository access flow you received with purchase.

## 2. Require the package

```bash
composer require lrakauskas/nativephp-google-admob
```

## 3. Register the plugin

Register the plugin with NativePHP:

```bash
php artisan native:plugin:register lrakauskas/nativephp-google-admob
```

## 4. Publish config

```bash
php artisan vendor:publish --tag=nativephp-google-admob-config
```

## 5. (optional) Add JS bridge

If you want to call plugin methods from JS, or want easier way to subscribe to plugin events, add the JS bridge to your `package.json`:

```json
{
  "imports": {
    "#nativephp": "./vendor/nativephp/mobile/resources/dist/native.js",
    "#lrakauskas/nativephp-google-admob": "./vendor/lrakauskas/nativephp-google-admob/resources/js/nativephpGoogleAdmob.js"
  }
}
```
