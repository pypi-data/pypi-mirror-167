# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from .xuproc import applyXUpdate
from lxml import etree
import sys

def main():
  from optparse import OptionParser
  usage = "usage: %prog xupdate_path document_path"
  parser = OptionParser(usage=usage)

  options, args = parser.parse_args()

  if len(args) != 2:
    parser.print_help()
    parser.error('incorrect number of arguments')
    sys.exit(2)

  xu_xml_name = args[0]
  doc_xml_name = args[1]

  print(etree.tostring(applyXUpdate(xml_xu_filename=xu_xml_name,
                                    xml_doc_filename=doc_xml_name),
                       pretty_print=True))
