# Installation

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

For premium package installs, use the repository access flow you received with purchase.

## 2. Require the package

```bash
composer require lrakauskas/nativephp-google-admob
```

## 3. Register the plugin

Add the service provider to `app/Providers/NativeServiceProvider.php`:

```php
public function plugins(): array
{
    return [
        \lrakauskas\NativephpGoogleAdmob\AdMobServiceProvider::class,
    ];
}
```

## 4. Publish config

```bash
php artisan vendor:publish --tag=nativephp-google-admob-config
```

## 5. Rebuild native artifacts when needed

If you change banner enablement state after installing the plugin, run:

```bash
php artisan native:install --force
```
