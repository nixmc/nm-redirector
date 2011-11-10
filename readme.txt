== Redirector ==

A flask app that redirects to any URL passed in:

http://example.com/http%3A%2F%2Fwww.google.com%2F

It also takes any random argument on the end to fool URL shorteners into generating a unique URL.

http://example.com/http%3A%2F%2Fwww.google.com%2F/fooling

If the bitly bot hits the app it should stop it from following the redirect.

See it in action: http://nm-redirector.herokuapp.com/