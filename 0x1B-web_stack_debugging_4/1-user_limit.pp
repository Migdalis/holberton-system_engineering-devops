# Fix error Too Many Open Files nginx to user holberton

exec { 'change-limits':
  command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 30000/' /etc/security/limits.conf &&
  sed -i 's/holberton soft nofile 4/holberton soft nofile 30000/' /etc/security/limits.conf",
  provider => shell
}
