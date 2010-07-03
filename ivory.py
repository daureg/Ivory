#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Ivory Launcher."""
import Game, Const, gettext
gettext.install('ivory', Const.LOCALE_DIR, unicode=True)
Game.Game().run()
