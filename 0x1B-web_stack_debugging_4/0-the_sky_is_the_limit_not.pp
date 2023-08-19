# 0. Sky is the limit, let's bring that limit higher

exec {'increase-Ulimit':
    command => "sed -i 's/15/4096' /etc/default/nginx",
    path => ['/bin/:/usr/local/bin'],
    notify => Exec['restart-nginx'],
}

exec {'restart-nginx':
    command => 'nginx restart',
    path => ['/etc/init.d/'],
    refreshonly => true,
}
