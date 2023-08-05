# -*- coding:utf-8 -*-

import os
import threading

from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.week import DEBUGGER, VERSIONS, ENVIRONMENT_VARIABLE_TEMP
from typing import Optional


class ILogging(object):
    '''the logging class'''
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(ILogging, "_instance"):
            with ILogging._instance_lock:
                if not hasattr(ILogging, "_instance"):
                    ILogging._instance = object.__new__(cls)
        return ILogging._instance

    def __init__(self):
        super(ILogging, self).__init__()

    def set_logging(self, dvs_file_name='log', dvs_logging_name='log', *paths):  # type: (str, str, *str) -> None
        'the set logging method'
        dvs_out = None  # type: Optional[str]
        if paths:
            dvs_out = os.path.join(os.getcwd(), *paths)  # type: ignore
            if dvs_out and not os.path.exists(dvs_out):
                os.makedirs(dvs_out)
        elif ENVIRONMENT_VARIABLE_TEMP in os.environ:
            dvs_out = os.getenv(ENVIRONMENT_VARIABLE_TEMP, None)
            if dvs_out and not os.path.exists(dvs_out):
                os.makedirs(dvs_out)
        else:
            dvs_out = os.path.join(os.getcwd(), 'out')
        if DEBUGGER:
            logging.set_kw_output_dir_name(dvs_out).set_kw_file_name(dvs_file_name).set_kw_level(
                logging.DEBUG).set_logging_formatter(
                    format_style=logging.DEBUG).set_logging_name(dvs_logging_name).build()
        else:
            logging.set_kw_output_dir_name(dvs_out).set_kw_file_name(dvs_file_name).set_kw_level(
                logging.DEBUG).set_logging_name(dvs_logging_name).build(console_only=False)
        if dvs_out and os.path.exists(dvs_out) and ENVIRONMENT_VARIABLE_TEMP in os.environ and dvs_out == os.getenv(
                ENVIRONMENT_VARIABLE_TEMP, None):
            logging.info('the currently found environment configuration variable({}: {}).'.format(
                ENVIRONMENT_VARIABLE_TEMP, dvs_out))
        logging.info('the current application version is {}.'.format(VERSIONS))


LOGGING = ILogging()
