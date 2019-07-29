#!/usr/bin/env python2
# -*- coding: iso-8859-1 -*-
#
# Impressive, a fancy presentation tool
# Copyright (C) 2005-2018 Martin J. Fiedler <martin.fiedler@gmx.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__title__   = "Impressive"
__version__ = "0.12.1-WIP"
__rev__     = None
__author__  = "Martin J. Fiedler"
__email__   = "martin.fiedler@gmx.net"
__website__ = "http://impressive.sourceforge.net/"

import sys
if __rev__ and (("WIP" in __version__) or ("rc" in __version__) or ("alpha" in __version__) or ("beta" in __version__)):
    __version__ += " (SVN r%s)" % __rev__
def greet():
    print("Welcome to", __title__, "version", __version__, file=sys.stderr)
if __name__ == "__main__":
    greet()


exec(compile(open("src/defaults.py", "rb").read(), "src/defaults.py", 'exec'), globals())
exec(compile(open("src/init.py", "rb").read(), "src/init.py", 'exec'), globals())
exec(compile(open("src/globals.py", "rb").read(), "src/globals.py", 'exec'), globals())
exec(compile(open("src/platform.py", "rb").read(), "src/platform.py", 'exec'), globals())
exec(compile(open("src/tools.py", "rb").read(), "src/tools.py", 'exec'), globals())
exec(compile(open("src/glcore.py", "rb").read(), "src/glcore.py", 'exec'), globals())
exec(compile(open("src/shaders.py", "rb").read(), "src/shaders.py", 'exec'), globals())
exec(compile(open("src/gltools.py", "rb").read(), "src/gltools.py", 'exec'), globals())
exec(compile(open("src/transitions.py", "rb").read(), "src/transitions.py", 'exec'), globals())
exec(compile(open("src/osdfont.py", "rb").read(), "src/osdfont.py", 'exec'), globals())
exec(compile(open("src/pdfparse.py", "rb").read(), "src/pdfparse.py", 'exec'), globals())
exec(compile(open("src/cache.py", "rb").read(), "src/cache.py", 'exec'), globals())
exec(compile(open("src/render.py", "rb").read(), "src/render.py", 'exec'), globals())
exec(compile(open("src/scriptwriter.py", "rb").read(), "src/scriptwriter.py", 'exec'), globals())
exec(compile(open("src/gldraw.py", "rb").read(), "src/gldraw.py", 'exec'), globals())
exec(compile(open("src/control.py", "rb").read(), "src/control.py", 'exec'), globals())
exec(compile(open("src/evcore.py", "rb").read(), "src/evcore.py", 'exec'), globals())
exec(compile(open("src/overview.py", "rb").read(), "src/overview.py", 'exec'), globals())
exec(compile(open("src/event.py", "rb").read(), "src/event.py", 'exec'), globals())
exec(compile(open('src/filelist.py', "rb").read(), 'src/filelist.py', 'exec'), globals())
exec(compile(open('src/main.py', "rb").read(), 'src/main.py', 'exec'), globals())
exec(compile(open("src/options.py", "rb").read(), "src/options.py", 'exec'), globals())


# use this function if you intend to use Impressive as a library
def run():
    try:
        run_main()
    except SystemExit as e:
        return e.code

# use this function if you use Impressive as a library and want to call any
# Impressive-internal function from a second thread
def synchronize(func, *args, **kwargs):
    CallQueue.append((func, args, kwargs))
    if Platform:
        Platform.ScheduleEvent("$call", 1)

if __name__ == "__main__":
    try:
        ParseOptions(sys.argv[1:])
        run_main()
    finally:
        if not(CleanExit) and (os.name == 'nt') and getattr(sys, "frozen", False):
            print()
            input("<-- press ENTER to quit the program --> ")
