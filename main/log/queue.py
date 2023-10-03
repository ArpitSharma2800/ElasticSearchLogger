from flask import request
from celery import Celery
from logES import process_log

celery = Celery(__name__, broker='redis://localhost:6379/0')

class Queue:
    @staticmethod
    def queueElasticLogger(user_id, opid, log_type, log_level, error, message):
        try:
            celery.send_task('process_log', args=[user_id, opid, log_type, log_level, error, message])
        except Exception as e:
            print(f"Failed to enqueue the log task: {str(e)}")
