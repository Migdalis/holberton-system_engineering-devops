# Fix error Too Many Open Files nginx

exec { 'worker_processes':
  command  => "sed -i 's/worker_processes 4;/worker_processes 7;/' /etc/nginx/nginx.conf",
  provider => shell
} ->

exec { 'nginx-restart':
  command  => 'sudo service nginx start',
  provider => shell
}
