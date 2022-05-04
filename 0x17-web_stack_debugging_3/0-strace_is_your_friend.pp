#!/usr/bin/env bash
# Fix error in wordpress settings

exec { 'wp-bug':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
