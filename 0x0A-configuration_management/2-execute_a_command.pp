#resource to kill the "killmenow" process using pkill
exec { 'killmenow':
  path    =>  '/bin/',
  command =>  'pkill killmenow',
  onlyif  =>  'pgrep -x killmenow',
}
