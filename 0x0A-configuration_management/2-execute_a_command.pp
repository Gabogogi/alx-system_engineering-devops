#resource to kill the "killmenow" process using pkill
exec { 'killmenow':
  command =>  'pkill killmenow',
  onlyif  =>  'pgrep -x killmenow',
}
