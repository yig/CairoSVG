#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is part of CairoSVG
# Copyright © 2010-2011 Kozea
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CairoSVG.  If not, see <http://www.gnu.org/licenses/>.

"""
CairoSVG entry point.

"""

import os
import sys
import optparse

import cairosvg


# Get command-line options
parser = optparse.OptionParser("usage: %prog filename [options]")
parser.add_option(
    "-v", "--version", action="store_true",
    default=False, help="show version and exit")
parser.add_option(
    "-f", "--format", help="output format")
parser.add_option(
    "-d", "--dpi", help="svg resolution")
parser.add_option(
    "-o", "--output",
    default="", help="output filename")
options, args = parser.parse_args()

# Print version and exit if the option is given
if options.version:
    print(cairosvg.VERSION)
    sys.exit()

# Set the resolution
if options.dpi:
    cairosvg.surface.DPI = float(options.dpi)

# Parse the SVG
format = options.format or os.path.splitext(options.output)[1].lstrip(".") or "pdf"
launcher = getattr(cairosvg, "svg2%s" % format)

# Print help if no argument is given
if not args:
    parser.print_help()
    sys.exit()

content = launcher(args[0])
if options.output:
    open(options.output, "w").write(content)
else:
    print(content)