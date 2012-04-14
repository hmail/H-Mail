# H-Mail

The E-Mail system we use today was created 30 years ago, and it's been showing its' age for a long time. Every internet user saw (and probably didn't understand) a message from the famous "Mail Delivery System", and every server administrator knows how hard and complicated it is to setup a mail service that's working.

H-Mail is here to change all that. It offers a new mailing system based on techniques we all know and use. It's something new which meant to replace E-Mail, and it has a great potential because of it's awesome features:

* It's unbelievably simple. Writing an H-Mail server is a matter of a few SLOC. Supporting H-Mail in your desktop application / in your web application is a breeze.
* It's uses HTTP, REST and JSON. You can probably guess the API yourself.
* It's doesn't conflict with E-Mail. You can have both, you can use one and gateway - whatever you want.
* It will save you hours of administration.

We believe H-Mail should replace E-mail, and we believe it's possible.

## Join us
H-Mail isn't just a cool idea. We really want to get rid of the old E-Mail and we need your help to do that.

* **Are you a user?** Get yourself an H-Mail account! Tell your friends about it!
* **Are you a developer?** Let your users use H-Mail instead of E-Mail. You'll write a few more lines today, but it will save you hundred when E-Mail will be gone. Also, why not adding H-Mail support to your favorite mail desktop application?
* **Are you a server administrator?** Run an H-Mail server on your server. It's so lightweight, and maybe one day you can git rid of that old E-Mail server you're wasting your time on.

## How does it work
H-Mail is all about simplicity, and it's designed with REST in mind. We use HTTP status codes intensively, and all repsonses are formatted in JSON. Every request and response includes at least one variable - the protocol version.

### Sending a mail

#### Request
An H-Mail to someone#example.com looks like this:

    POST example.com:26/someone/
    
    {'title': 'Welcome aboard!',
     'content': 'You are now part of H-Mail',
     'sender': 'someone#somewhere.com',
     'recipient: 'someone#example.com',
     'protocol': 0.1}

#### Response
If the mail was accpeted, the server reponses with a simple HTTP 201 Created:

    HTTP 201

    {'protocol': 0.1}

In case of an error, the server uses one of the following:

* 413 - The message exceeded the maximum size the server accpets
* 404 - The recipient does not exist on the server
* 401 - You have been banned from the server (optional: speicify contact information)
* 429 - You sent too many mails in a short time. You can retry again later.
* 507 - The recipient is out of space. You can retry again later.
* 426 - Server only recives messages over HTTPS.

### Getting a list of mails for an account
#### Request

    GET server.com:26/user/ (listing)

* 200 - list (JSON)
* 304 - cached
* 401 - not authorised

### Reading a mail
#### Request

    GET server.com:26/user/123 (e-mail content)

#### Response

* 200 - mail content (JSON)
* 304 - cached
* 401 - not authorised
* 404 - no such mail
* 410 - was removed

### Deleting a mail:
#### Request

    DELETE server.com/user/123

#### Response

* 200 - ok
* 401 - not authorised
* 404 - no such mail
* 410 - was removed

### Marking mail as read/unread/spam:
#### Request

    PUT server.com/user/123

#### Response

* 200 - ok
* 401 - not authorised
* 404 - no such mail
* 410 - was removed


# Use H-Mail
## H-Mail Servers

* Tornadail (Python, Tornado based, database agnostic)
* Write your own!

## Web applications

* Write your own!

## Desktop applications

* Patch your favourite application!

# Conclusion

The H-Mail protocol is under development, and this is it's first draft. Besides implementing it, we will be happy to know what you think about it. Contact us.

# Inspirions and Prior art

* http://mailnuggets.com/pages/features/email_over_http_post
* http://webhooks.wordpress.com/2009/02/13/restful-email-over-http/

# TODO

* Tags and other mail properties
* Authentication
* Forwarding standard?
* Attachments, other types rather than message (i.e. sending a reminder)