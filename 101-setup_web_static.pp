# Manifest that configures a web server for deployment
exec { 'process_0':
  command => 'sudo sudo apt-get update -y',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'process_1':
  require => Exec['process_0'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'process_2':
  require => Exec['process_1'],
  command => 'sudo mkdir -p /data/web_static/shared/',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'process_3':
  require => Exec['process_2'],
  command => 'sudo mkdir -p /data/web_static/releases/test/',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'process_4':
  require => Exec['process_3'],
  command => 'sudo touch /data/web_static/releases/test/index.html',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'process_5':
  require => Exec['process_4'],
  command => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html >/dev/null',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'process_6':
  require => Exec['process_5'],
  command => 'rm -rf /data/web_static/current',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0,1]
}


exec { 'process_7':
  require => Exec['process_6'],
  command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0,1]
}

exec { 'process_8':
  require => Exec['process_7'],
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0,1]
}

exec { 'process_9':
  require     => Exec['process_8'],
  environment => ['C=\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n'],
  command     => 'sudo sed -i "38i $C" /etc/nginx/sites-available/default',
  path        => ['/usr/bin'],
  returns     => [0,1]
}

exec { 'process_10':
  require => Exec['process_9'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0,1]
}
