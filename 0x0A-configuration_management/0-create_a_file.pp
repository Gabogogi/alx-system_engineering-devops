#creates a file in tmp, sets mode, users and permissions
file { 'tmp/school' :
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
