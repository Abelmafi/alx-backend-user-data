#!/usr/bin/env python3
""" Task1: Write a function called filter_datum
that returns the log message obfuscated:"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate specified fields in a log message.
    """
    pattern = r'(?<={0})[^{1}]+(?={1})'.format(separator, separator)
    return re.sub(pattern, redaction, message)
