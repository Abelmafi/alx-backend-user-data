#!/usr/bin/python3
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate specified fields in a log message.
    """
    pattern = r'(?<={0})[^{1}]+(?={1})'.format(separator, separator)
    return re.sub(pattern, redaction, message)
