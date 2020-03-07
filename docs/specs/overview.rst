.. doctest docs/specs/overview.rst
.. _amici.specs.overview:

===================
Lino Amici Overview
===================


.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_amici.projects.herman.settings.demo')
>>> from lino.api.doctest import *


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 39 plugins
- 60 models
- 19 user roles
- 6 user types
- 220 views
- 18 dialog actions
<BLANKLINE>


User types
==========

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

>>> ses = rt.login('robin')
>>> ses.user.user_type
users.UserTypes.admin:900
>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Households, Partner Lists
- Office : Data problems assigned to me, My Blog Entries, My Excerpts, My Comments, Recent comments, My Upload files
- Calendar : My appointments, Overdue appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Configure :
  - System : Users, Site Parameters, Help Texts
  - Contacts : Organization types, Functions, Household Types, List Types
  - Calendar : Calendars, Rooms, Recurring events, Guest roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows
  - Topics : Topics
  - Blog : Blog Entry Types
  - Office : Excerpt Types, My Text Field Templates, Comment Types, Library volumes, Upload types
  - Places : Countries, Places
- Explorer :
  - System : Authorities, User types, User roles, Data checkers, Data problems, All dashboard widgets, content types
  - Contacts : Contact Persons, Partners, Address types, Addresses, Contact detail types, Contact details, Household member roles, Household Members, Personal Links, Parency types, List memberships
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Entry states, Presence states, Task states
  - SEPA : Bank accounts
  - Topics : Interests
  - Blog : Blog Entries
  - Office : Excerpts, Text Field Templates, Comments, Mentions, Upload files, Upload areas
- Site : About
