# -*- coding:utf-8 -*-

import os
import threading

from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.config import DEBUGGER, VERSIONS, ENVIRONMENT_VARIABLE_TEMP
from typing import Callable, Optional


class ICliLogging(object):
    '''the logging class with cli'''
    _instance_lock = threading.Lock()  # protected static property

    def __new__(cls, *args, **kwargs):
        if not hasattr(ICliLogging, "_instance"):
            with ICliLogging._instance_lock:
                if not hasattr(ICliLogging, "_instance"):
                    ICliLogging._instance = object.__new__(cls, *args, **kwargs)
        return ICliLogging._instance

    def __init__(self):
        super(ICliLogging, self).__init__()

    def set_logging(self,
                    dvs_file_name='log',
                    dvs_logging_name='root',
                    on_callback=None,
                    *paths,
                    **kwargs):  # type: (str, str, Optional[Callable[..., None]] ,*str, ...) -> None
        '''
            the set logging method

            dvs_file_name: the file name
            dvs_logging_name: the logging instance name that is recommended package name for the current run application
            paths: the logging relative file path
            kwargs: {
                logging_level: int that is com.dvsnier.config.journal.compat_logging.logging.WARNING
                logging_formatter: str that default is '[%(asctime)s][%(levelname)8s][%(process)d-%(thread)d][%(name)s] --- %(message)s'
                logging_format_style: int that is com.dvsnier.config.journal.compat_logging.logging.WARNING
                logging_console_only: False
                logging_file_record: True
                logging_error_record: True
            }
        '''
        # region dvs_out
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
        # endregion
        # region the pre callback
        if on_callback:
            on_callback(dvs_file_name, dvs_logging_name, dvs_out, kwargs)
        # endregion
        logging.set_kw_output_dir_name(dvs_out)
        logging.set_kw_file_name(dvs_file_name)
        logging.set_logging_name(dvs_logging_name)
        logging_level = logging.WARN  # type: int
        if DEBUGGER:
            logging_level = logging.DEBUG
        if kwargs:
            logging_level = kwargs.get('logging_level', logging.WARN)
            logging_formatter = kwargs.get('logging_formatter', '[%(asctime)s][%(levelname)8s][%(process)d-%(thread)d][%(name)s] --- %(message)s')
            logging_format_style = kwargs.get('logging_format_style', logging.WARNING)
            console_only = kwargs.get('logging_console_only', False)
            file_record = kwargs.get('logging_file_record', True)
            error_record = kwargs.get('logging_error_record', True)
            logging.set_kw_level(logging_level)
            logging.set_logging_formatter(logging_formatter, logging_format_style)
            logging.build(console_only, file_record, error_record)
        else:
            logging.set_kw_level(logging_level).build(console_only=False)
        if dvs_out and os.path.exists(dvs_out) and ENVIRONMENT_VARIABLE_TEMP in os.environ and dvs_out == os.getenv(
                ENVIRONMENT_VARIABLE_TEMP, None):
            logging.info('the currently found environment configuration variable({}: {}).'.format(
                ENVIRONMENT_VARIABLE_TEMP, dvs_out))
        logging.info('the current application version is {}.'.format(VERSIONS))


LOGGING = ICliLogging()
