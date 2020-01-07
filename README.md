**TwitterAccMon** Is a Simple Twitter Account Monitor, run from a cronjob it becomes a Monitoring and Alert agent.
It will tell you within seconds when an account is live, and keep checking for if they go offline.

**Python3**
```
pip3 install smtplib requests datetime
```

**Configure Your Email Settings**
```
from_email = 'yourfromemail@example.com' #Your Email
to_email = 'wheryouwantosendtheemail@example.com' #Your Email
email_user = 'emailuser@example.com' #Your Email
email_pass = 'yourpassword' #Your Email Password
smtp_server = 'smtp.gmail.com'
smtp_port = '587' #Your SMTP port
```

**Configure Your Users**
Add Users to monitor like the example below, remove the @
```
user_mon_list = ['account1','account2']
```

**Install in a cron job**
```
crontab -e
* * * * * python3 /path/to/your/TwitAccMon.py
```

**Author**

* **Joshua Whitaker** 
* *Twitter* [@_Stahlz](https://twitter.com/_Stahlz)
* *Email* - [stahl@stahl.io](stahl@stahl.io)
* *Website* - [stahl.io](https://www.stahl.io)



