##############################################################################
#
# Copyright (c) 2017 Shoobx, Inc.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""RML to DOCX Converter Interfaces
"""
import zope.interface

class IRML2DOCX(zope.interface.Interface):
    """This is the main public API of shoobx.rml2docx"""

    def parseString(xml):
        """Parse an XML string and convert it to DOCX.

        The output is a ``StringIO`` object.
        """

    def go(xmlInputName, outputFileName=None, outDir=None):
        """Convert RML to DOCX.

        The generated file will be located in the ``outDir`` under the name
        ``outputFileName``.
        """