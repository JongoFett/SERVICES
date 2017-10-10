# Run service

I created this as I was having issues with SSH running and was paranoid about DDClient not running.

Though I am sure there are simpler and easier ways to make sure they're always running I decided to play wiht Python in order to create a file which would check to see if they're running, if they are then it leaves them alone. If they're not running then it runs them.

To get the services to run without having to type in the root password though I had to make some changes in the visduo file to make sure my user could run those commands without needing a password.

## NOTE
Making these changes was something I was happy doing but is likely not best practice so only use this if you're comfortable making those changes.

### Changes to visduo
'''
<br>
<username> ALL=NOPASSWD: /bin/systemctl start service0 <br>
<username> ALL=NOPASSWD: /bin/systemctl start service1<br>
'''
#### where <> use your own username
#### where 'service#' insert your desired service

Thank you for taking the time to look at my work.

-JongoFett
