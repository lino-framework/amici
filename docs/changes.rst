.. _amici.changes: 

========================
Changes in Lino Amici
========================

2019-07-13
==========

Activated the possibility to enable automatic presences on a calendar entry
type (:ticket:`3119`). Until now, checking the
:attr:`lino_xl.lib.cal.EventType.force_guest_state` option had no effect since
the entry states did not know which guest state to set when it was enabled.

Added :class:`lino_xl.lib.cal.EntriesByGuest` to the detail view of a person.

2017-05-05
==========

First publication.
