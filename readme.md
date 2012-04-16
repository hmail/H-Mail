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
H-Mail is all about simplicity, and it's designed with REST in mind. We use HTTP status codes intensively, and all responses are formatted in JSON. Every request and response includes at least one variable - the protocol version.

### Sending a mail

#### Request
An H-Mail to someone#example.com looks like this:

    POST example.com:26/someone/
    
    {"title": "Welcome aboard!",
     "content": "You are now part of H-Mail",
     "sender": "someone#somewhere.com",
     "recipient: "someone#example.com",
     "protocol": 0.1}

#### Response
If the mail was accepted, the server responses with a simple HTTP 201 Created:

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8

    {'protocol': 0.1}

In case of an error, the server uses one of the following:

* 413 - The message exceeded the maximum size the server accepts
* 404 - The recipient does not exist on the server
* 401 - You have been banned from the server (optional: specify contact information)
* 429 - You sent too many mails in a short time. You can retry again later.
* 507 - The recipient is out of space. You can retry again later.
* 426 - Server only receives messages over HTTPS.

### Getting a list of mails for an account
#### Request

    GET /user/
    Host: server.com:26
    Accept: text/json

You can specify these GET parameters in the request:

* limit - Limit the amount of messages in the list. Default: 15
* order - Order the message by 'sender', 'recpient', 'time' or 'title'. Adding negative sign at the beginning indicates descending order. Default: "-time"
* offset - Start listing from object #x. Default: 0
* summary - Include a plaintext version of the message's content. Default: false

#### Response

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8

    {
      "limit": 15,
      "order": "-time",
      "offset": 0,
      "messages": [
                    {
                      "sender": "someone#somewhere.com",
                      "recipient": "someone@example.com",
                      "time": "2012-04-13 22:46:35",
                      "title": "Welcome to H-Mail!",
                      "read": true,
                      "id": 1
                    },
                    {
                      "sender": "someone@example.com",
                      "recipient": "someone#somewhere.com",
                      "time": "2012-04-13 22:46:36",
                      "title": "How do you like H-Mail so far?",
                      "read": false,
                      "id": 2
                    }
                  ]
    }

Other possible responses are:

* 304 Not Modified - Message has not been modified since last requested
* 401 Unauthorized - Client didn't authenticate or it failed to do so
* 426 Upgrade Required - Server only operates over HTTPS

### Reading a mail
#### Request

    GET /user/123
    Host: server.com:26
    Accept: text/json

#### Response

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8

    {
      "title": "Welcome aboard!",
      "sender": "someone#somewhere.com",
      "recipient: "someone#example.com",
      "content": [
                    {
                      "content-type": "text/plain",
                      "charset": "UTF-8",
                      "content": "You are now part of H-Mail"
                    }
                 ]
      "protocol": 0.1
    }

 Content can include as many objects as you want, and of *any kind*. It can have be text/html, text/calendar, or anything else really. If your client knows how to display it, it will, and if not, it will show up as an attachment with the title as the filename.

 Attachments are also handled in this way, except they include one more property: filename. That's how you can distinguish between a message and the text file that came with it:

     "content": [
                  {
                    "content-type": "text/plain",
                    "charset": "UTF-8",
                    "content": "this should be displayed by the client"
                  },
                  {
                    "filename": "somefile.txt"
                    "content-type": "text/plain",
                    "charset": "UTF-8",
                    "content": "this is just an attachment"
                  }
                ]

Other possible responses are:
* 304 Not Modified - Message has not been modified since last requested
* 401 Unauthorized - Client didn't authenticate or it failed to do so
* 404 Not Found - Message doesn't exist
* 410 Gone - Message was removed
* 426 Upgrade Required - Server only operates over HTTPS


### Deleting a mail:
#### Request

    DELETE /user/123
    Host: server.com:26
    Accept: text/json

#### Response

* 200 - ok
* 401 - not authorised
* 404 - no such mail
* 410 - was removed

### Marking mail as read/unread/spam:
#### Request

    PUT /user/123
    Host: server.com:26
    Accept: text/json

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
* Get without attachments (default?)