# Puppet ssh config
exec { 'disable_password_authentication':
  command  => "echo 'PasswordAuthentication no' >> /etc/ssh/ssh_config",
  provider => 'shell',
}
exec { 'set_identity_file':
  command  => "echo 'IdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
  provider => 'shell',
}
