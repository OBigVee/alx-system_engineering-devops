# kills a process called "killmenow"
exec { 'killmenow':
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
