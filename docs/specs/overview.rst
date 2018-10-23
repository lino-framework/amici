.. doctest docs/specs/overview.rst
.. _amici.specs.overview:

===================
Lino Amici Overview
===================


.. contents:: 
   :local:
   :depth: 2

>>> from lino import startup
>>> startup('lino_amici.projects.herman.settings.demo')
>>> from lino.api.doctest import *


>>> rt.show(users.UserTypes)
======= =========== =================
 value   name        text
------- ----------- -----------------
 000     anonymous   Anonymous
 100     user        User
 200     collector   Collector
 300     manager     Project manager
 800     staff       Staff
 900     admin       Administrator
======= =========== =================
<BLANKLINE>

