from flask import request
import threading
import time


class LogAPI:

    def _validate_data(self, data):
        user_id = data.get('user_id')
        opid = data.get('opid')
        log_type = data.get('log_type')
        log_level = data.get('log_level')
        error = data.get('error')
        message = data.get('message')

        if any(field is None for field in [user_id, opid, log_type, log_level, message]):
            return False

        allowed_log_levels = ['info', 'warning', 'error', 'verbose', 'trivia']
        if log_level not in allowed_log_levels:
            return False

        if error is None:
            error = ''

        return True

    @staticmethod
    def post(self):
        response_thread = threading.Thread(target=self.send_response)
        response_thread.start()

        data = request.json

        if not self._validate_data(data):
            print("checked")

        user_id = data.get('user_id')
        opid = data.get('opid')
        log_type = data.get('log_type')
        log_level = data.get('log_level')
        error = data.get('error')
        message = data.get('message')

    def send_response(self):
        time.sleep(0.1)
        return "Log message submitted!", 200
