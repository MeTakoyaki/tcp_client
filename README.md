# Server TCP  
simple python based TCP client

## Penjelasan : 

![Screenshoot] (img-asset/code-screenshoot.png)

Countless times during penetration tests, we (the authors) have
needed to whip up a TCP client to test for services, send garbage
data, fuzz, or perform any number of other tasks. If you are working
within the confines of large enterprise environments, you won’t have
the luxury of using networking tools or compilers, and sometimes
you’ll even be missing the absolute basics, like the ability to
copy/paste or connect to the internet. This is where being able to
quickly create a TCP client comes in extremely handy. But enough
jabbering—let’s get coding.

We first create a socket object with the AF_INET and SOCK_STREAM
parameters 1. The AF_INET parameter indicates we’ll use a standard
IPv4 address or hostname, and SOCK_STREAM indicates that this will be
a TCP client. We then connect the client to the server 2 and send it
some data as bytes 3. The last step is to receive some data back
and print out the response 4 and then close the socket. This is the
simplest form of a TCP client, but it’s the one you’ll write most often.

This code snippet makes some serious assumptions about
sockets that you definitely want to be aware of. The first assumption
is that our connection will always succeed, and the second is that the
server expects us to send data first (some servers expect to send
data to you first and await your response). Our third assumption is
that the server will always return data to us in a timely fashion. We
make these assumptions largely for simplicity’s sake. While
programmers have varied opinions about how to deal with blocking
sockets, exception-handling in sockets, and the like, it’s quite rare for
pentesters to build these niceties into their quick-and-dirty tools for
recon or exploitation work, so we’ll omit them in this chapter.