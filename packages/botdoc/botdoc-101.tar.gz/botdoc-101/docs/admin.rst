.. _admin:


.. raw:: html

  <br>


.. title:: admin


**ADMIN**


CONFIGURATION


 configuration is done by calling the ``cfg`` command of the bot.

 **irc**

 | ``bot cfg server=<server> channel=<channel> nick=<nick>``

 | (*) default channel/server is #botd on localhost

 **sasl**

 | ``bot pwd <nickservnick> <nickservpass>``
 | ``bot cfg password=<outputfrompwd>``

 **users**

 | ``bot cfg users=True``
 | ``bot met <userhost>``


 **rss**

 | ``bot rss <url>``
 |

SYSTEMD

 to run the bot after reboot, install the service file and start the service
 by enabling it with ``--now``.

 | $ ``sudo cp /usr/local/share/botd/botd.service /etc/systemd/system``
 | $ ``sudo systemctl enable botd --now``

 | (*) default channel/server is #botd on localhost

 use ``botctl`` instead of the use ``bot`` program

 | $ ``sudo botctl cfg server=<server> channel=<channel> nick=<nick>``
 | $ ``sudo botctl pwd <nickservnick> <nickservpass>``
 | $ ``sudo botctl cfg password=<outputfrompwd>``
 | $ ``sudo botctl cfg users=True``
 | $ ``sudo botctl met <userhost>``
 | $ ``sudo botctl rss <url>``
 |

COMMANDS

 here is a short description of the commands.

 | ``cmd`` - shows all commands
 | ``cfg`` - shows the irc configuration, also edits the config
 | ``dlt`` - removes a user from bot
 | ``dpl`` - sets display items for a rss feed
 | ``ftc`` - runs a rss feed fetching batch
 | ``fnd`` - allows you to display objects on the datastore, read-only json files on disk 
 | ``flt`` - shows a list of bot registered to the bus
 | ``log`` - logs some text
 | ``met`` - adds a users with there irc userhost
 | ``mre`` - displays cached output, channel wise.
 | ``nck`` - changes nick on irc
 | ``pwd`` - combines a nickserv name/password into a sasl password
 | ``rem`` - removes a rss feed by matching is to its url
 | ``rss`` - adds a feed to fetch, fetcher runs every 5 minutes
 | ``thr`` - show the running threads
 | ``tdo`` - adds a todo item, no options returns list of todo's
