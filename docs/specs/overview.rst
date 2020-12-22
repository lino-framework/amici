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
>>> startup('lino_amici.projects.amici1.settings.demo')
>>> from lino.api.doctest import *


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 40 plugins
- 66 models
- 6 user types
- 251 views
- 21 dialog actions
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
<users.UserTypes.admin:900>
>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Households, Partner Lists
- Office : Data problems assigned to me, My Blog Entries, My Excerpts, My Comments, Recent comments, My Upload files
- Calendar : My appointments, Overdue appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Activities : My Activities, Activities, -, Activity lines, Pending requested enrolments, Pending confirmed enrolments
- Configure :
  - System : Users, Site Parameters, Help Texts
  - Contacts : Organization types, Functions, Household Types, List Types
  - Calendar : Calendars, Rooms, Recurring events, Guest roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows
  - Activities : Topics, Timetable Slots
  - Topics : Topics
  - Blog : Blog Entry Types
  - Office : Excerpt Types, My Text Field Templates, Comment Types, Library volumes, Upload types
  - Places : Countries, Places
- Explorer :
  - System : Authorities, User types, User roles, Data checkers, Data problems, All dashboard widgets, content types
  - Contacts : Contact persons, Partners, Address types, Addresses, Contact detail types, Contact details, Household member roles, Household Members, Personal Links, Parency types, List memberships
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Entry states, Presence states, Task states, Planner columns, Access classes, Display colors
  - SEPA : Bank accounts
  - Activities : Activities, Enrolments, Enrolment states, Course layouts, Activity states
  - Topics : Interests
  - Blog : Blog Entries
  - Office : Excerpts, Text Field Templates, Comments, Mentions, Reactions, Upload files, Upload areas
- Site : About


Activity layouts
================

>>> rt.show(courses.CourseAreas)
======= ========= ============ =================
 value   name      text         Table
------- --------- ------------ -----------------
 C       default   Activities   courses.Courses
======= ========= ============ =================
<BLANKLINE>



>>> rt.show(cal.EntryStates)
======= ============ ============ ============= ============= ======== ============= =========
 value   name         text         Button text   Fill guests   Stable   Transparent   No auto
------- ------------ ------------ ------------- ------------- -------- ------------- ---------
 10      suggested    Suggested    ?             Yes           No       No            No
 20      draft        Draft        ☐             Yes           No       No            No
 50      took_place   Took place   ☑             No            Yes      No            No
 70      cancelled    Cancelled    ☒             No            Yes      Yes           Yes
======= ============ ============ ============= ============= ======== ============= =========
<BLANKLINE>
