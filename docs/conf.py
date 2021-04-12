# -*- coding: utf-8 -*-
from lino.sphinxcontrib import configure
configure(globals(), 'lino_amici.projects.amici1.settings.demo')

extensions += ['lino.sphinxcontrib.logo']

project = "Lino Amici"
copyright = '2014-2021 Rumma & Ko Ltd'
html_title = "Lino Amici"
html_context.update(public_url='https://amici.lino-framework.org')
