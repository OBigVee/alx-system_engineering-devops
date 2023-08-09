# Strace command to debug apache2

exec { 'fix_typo_1':
  command => "sed -t 's/phpp/php/g' /var/www/html/wp-settings.php",
  path => '/bin',
}

exec { 'fix_typo_2':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path => '/usr/bin',
}
