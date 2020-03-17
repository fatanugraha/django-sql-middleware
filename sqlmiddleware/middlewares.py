import inspect
import json
import os
import re
import struct
import termios
import time
import traceback
import sys
import json
from datetime import datetime
from uuid import UUID
from django.conf import settings
import warnings

from django.conf import settings
from django.db import connection
from django.http import HttpResponse

from .globals import save_request


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class TracebackLogger:
    def __init__(self):
        self.tracebacks = []

    def capture_traceback(self):
        tb = ''.join(traceback.format_stack())
        self.tracebacks.append(tb)

    def __call__(self, execute, sql, params, many, context):
        start = time.monotonic()

        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            raise

        self.capture_traceback()
        return result


def get_explain(sql):
    with connection.cursor() as cursor:
        cursor.execute(f"EXPLAIN {sql}")
        return '\n'.join(r[0] for r in cursor.fetchall())


explain_cost_r = re.compile("\(cost=(?P<cost>[^ ]+) rows=(?P<rows>\d+) width=(?P<width>\d+)\)")


def LogSQLMiddleware(get_response):
    def should_capture(request):
        if 'sqlite' in settings.DATABASES['default']['ENGINE']:
            warnings.warn("Does not support sqlite yet")
            return False

        return True

    def middleware(request):
        if not should_capture(request):
            return get_response(request)

        logger = TracebackLogger()

        with connection.execute_wrapper(logger):
            response = get_response(request)

        queries = connection.queries.copy()

        for tb, q in zip(logger.tracebacks, queries):
            q['traceback'] = tb
            explain = get_explain(q['sql'])

            result = explain_cost_r.search(explain.split('\n')[0])
            q['explain'] = explain
            q['explain_cost'] = result.group("cost")
            q['explain_rows'] = result.group("rows")
            q['explain_width'] = result.group("width")

        total_duration = sum(float(q['time']) for q in queries)
        request_data = {
            'method': request.method,
            'created_at': datetime.now().isoformat(),
            'endpoint': request.build_absolute_uri(),
            'total_time': total_duration,
            'total_queries': len(queries),
            'paths': json.dumps(sys.path[1:]),
            'queries': queries,
        }
        if queries:
            save_request(request_data)

        return response

    return middleware
