# Set up client SSH configuration file

exec { 'ssh_config':
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => ['/usr/bin', '/bin'],
}
