.. _amici.specs.overview:

===================
Lino Amici Overview
===================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_overview
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_amici.projects.herman.settings.demo')
    >>> from lino.api.doctest import *

.. contents:: 
   :local:
   :depth: 2


>>> UserTypes = rt.models.users.UserTypes

>>> rt.show(UserTypes)
======= =========== ================= ================================================
 value   name        text              User role
------- ----------- ----------------- ------------------------------------------------
 000     anonymous   Anonymous         lino_amici.lib.amici.user_types.Anonymous
 100     user        User              lino_amici.lib.amici.user_types.EndUser
 200     collector   Collector         lino_amici.lib.amici.user_types.Collector
 300     manager     Project manager   lino_amici.lib.amici.user_types.ProjectManager
 800     staff       Staff             lino_amici.lib.amici.user_types.Staff
 900     admin       Administrator     lino_amici.lib.amici.user_types.SiteAdmin
======= =========== ================= ================================================
<BLANKLINE>

