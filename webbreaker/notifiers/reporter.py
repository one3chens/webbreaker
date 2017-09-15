#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webbreaker.webbreakerlogger import Logger


class Reporter(object):

    def __init__(self, notifiers):
        self.notifiers = notifiers

    def report(self, event):
        try:
            for notifier in self.notifiers:
                notifier.notify(event)
        except AttributeError as e:
            Logger.app.error("Error sending email. {}".format(e.message))
            Logger.console.error("Error sending email, see log: {}".format(Logger.app_logfile))
