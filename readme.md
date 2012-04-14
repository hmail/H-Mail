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
H-Mail is all about simplicity, and it's designed with REST in mind. We use HTTP status codes intensively, and when there's need for data response we're using JSON.

### Sending a mail

#### Request
An H-Mail to someone#example.com looks like this:

    POST example.com:26/someone/
    
    {'title': 'Welcome aboard!',
     'content': 'You are now part of H-Mail',
     'sender': 'someone#somewhere.com',
     'recipient: 'someone#example.com'}

#### Response
If the mail was accpeted, the server reponses with HTTP 201 Created:

    HTTP 201

In case of an error, the server uses one of the following:

* 413 - The message exceeded the maximum size the server accpets
* 404 - The recipient does not exist on the server
* 401 - You have been banned from the server (optional: speicify contact information)
* 429 - You sent too many mails in a short time. You can ry again later.
* 507 - The recipient is out of space. You can ry again later.
* 426 - Server only recives messages over HTTPS.

### Getting a list of mails for an account
#### Request

    GET server.com:26/yoav/ (listing)

* 200 - list (JSON)
* 304 - cached
* 401 - not authorised

### Reading a mail
#### Request

    GET server.com:26/yoav/123 (e-mail content)

#### Response

* 200 - mail content (JSON)
* 304 - cached
* 401 - not authorised
* 404 - no such mail
* 410 - was removed

### Deleting a mail:
#### Request

    DELETE server.com/yoav/123

#### Response

* 200 - ok
* 401 - not authorised
* 404 - no such mail
* 410 - was removed

### Marking mail as read/unread/spam:
#### Request

    PUT server.com/yoav/123

#### Response

* 200 - ok
* 401 - not authorised
* 404 - no such mail
* 410 - was removed