#creates a file with the following resource declaration
# File path is /tmp/school
# File permission is 0744
# File owner is www-data
# File group is www-data
# File contains I love Puppet

file { 'tmp/school':
  ensure => file,
  path   => '/tmp/school',
  cotent => 'I love Puppet',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744',
}
