#!/usr/bin/python3

import random
import json
import logging
from icons import base

class Report:
    '''A Report is a set of icons representing something to report.
It has a banner icon and a list of values, each of which is either an icon or a list of frames.'''
    def __init__(self, *icons, banner=None):
        self.banner = banner
        self.icons = icons

    def __iter__(self):
        for i in self.icons:
            yield i

    def __len__(self):
        return len(self.icons)

class DataSource:
    '''No help for this API.'''
    CHOICES = {}

    @staticmethod
    def define_args(parser):
        pass

    def __getitem__(self, p):
        return self.args.get(p, None)

    def __init__(self, **args):
        self.args = args
        if not hasattr(self,"banner"):
            self.banner = base.digit_banner


class FileDataSource(DataSource):
    @staticmethod
    def define_args(parser):
        parser.add_argument("filename", type=str, help="Sample file name")
        DataSource.define_args(parser)

    def _readFile(self, bytes=-1):
        try:
            return open(self.filename,"r").read(bytes)
        except IOError:
            logging.warn("Couldn't read from file %s" % self.filename)
            return None

    def _readJSON(self):
        try:
            return json.load(open(self.filename,"r"))
        except (IOError, ValueError):
            logging.warn("Couldn't read JSON from file %s" % self.filename)
            return None

    def __init__(self, filename, **args):
        self.filename = filename
        DataSource.__init__(self, **args)

