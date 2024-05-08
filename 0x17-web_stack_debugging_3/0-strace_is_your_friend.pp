# Fixing the .php extension
exec { 'fix .phpp':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => 'shell',
}
