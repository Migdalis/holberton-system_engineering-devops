#!/usr/bin/env bash
# Fix error in wordpress settings

exec { 'wp-bug':
  command => 'sed -i /class-wp-locale.phpp/class-wp-locale.php /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
