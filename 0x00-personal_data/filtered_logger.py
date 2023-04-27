#!/usr/bin/env python3
""" Task1: Write a function called filter_datum
that returns the log message obfuscated:"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate specified fields in a log message.
    """
    pattern = re.compile(separator.join(f'({field}=)[^{separator}]*' for field in fields))
    return pattern.sub(f'\\1{redaction}', message)
