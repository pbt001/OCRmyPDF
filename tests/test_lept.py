# © 2018 James R. Barlow: github.com/jbarlow83
#
# This file is part of OCRmyPDF.
#
# OCRmyPDF is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OCRmyPDF is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OCRmyPDF.  If not, see <http://www.gnu.org/licenses/>.


import os
import shutil
import pytest
import sys
import ocrmypdf.leptonica as lept


def test_colormap_backgroundnorm(resources):
    # Issue #262 - unclear how to reproduce exactly, so just ensure leptonica
    # can handle that case
    pix = lept.Pix.open(resources / 'baiona-colormapped.png')
    pix.background_norm()
