# Killing a process
exec { 'killmenow':
  command  => 'pkill -f "killmenow"',
  provider => 'shell',
}
