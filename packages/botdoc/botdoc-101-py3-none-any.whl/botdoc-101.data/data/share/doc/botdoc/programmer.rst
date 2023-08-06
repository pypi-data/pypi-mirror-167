.. _programmer:

.. raw:: html

    <br>

.. title:: programmer


**PROGRAMMER**

The ``bot`` package provides an Object class (in bot.obj), that provides a
save/load to/from json files on disk. Objects can be searched with database
functions and read-only files to improve persistence are used. Types in filename
are used for reconstruction. Methods are factored out into functions to have a
clean namespace to read JSON data into.

basic usage is this::

>>> from bot.obj import Object
>>> o = Object()
>>> o.key = "value"
>>> o.key
>>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

>>> from bot.obj import Object
>>> from bot.jsn import load, save
>>> o = Object()
>>> o.key = "value"
>>> p = save(o)
>>> oo = Object()
>>> load(oo, p)
>>> oo.key
>>> 'value'

great for giving objects peristence by having their state stored in files.

>>> from bot.obj import Object, save
>>> from bot.wdr import Wd
>>> Wd.workdir = ".test"
>>> o = Object()
>>> save(o)
bot.obj.Object/e455c143-180e-4b43-bda2-9f09500cedba/2021-08-31/15:31:05.717063
