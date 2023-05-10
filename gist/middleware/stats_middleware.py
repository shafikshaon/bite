import logging
from functools import reduce
from operator import add
from socket import error as SocketError

from django.db import connection
from django.utils.deprecation import MiddlewareMixin

__author__ = "Shafikur Rahman"

import time

logger = logging.getLogger(__name__)


class StatsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        try:
            duration = time.time() - request.start_time
            db_queries = len(connection.queries)
            if db_queries:
                db_time = reduce(add, [float(q["time"]) for q in connection.queries[:]])
            else:
                db_time = 0.0

            db_time = float(db_time * 1000)
            total_time = float(duration * 1000)
            python_time = float(total_time - db_time)

            db_queries = db_queries

            response["X-Total-Time"] = round(total_time, 2)
            response["X-Python-Time"] = round(python_time, 2)
            response["X-DB-Time"] = round(db_time, 2)
            response["X-DB-Queries"] = db_queries
            res = (
                f"Total time(s): {response['X-Total-Time']}, Python time(s): "
                f"{response['X-Python-Time']}, DB time(s): {response['X-DB-Time']}, "
                f"DB-Queries count: {response['X-DB-Queries']}"
            )
            print(res)
            logger.info("This message should be logged")

            logger.log(1, f"Response {res}")
        except SocketError as e:
            print(e)
            pass
        return response
