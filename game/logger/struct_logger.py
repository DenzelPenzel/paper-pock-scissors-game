import json
import logging

from game.logger import log_encoder


class StructLogRecord(logging.LogRecord):
    def getMessage(self):
        """
        Return dict msg if present
        """
        if "dict_msg" in self.__dict__ and isinstance(self.__dict__["dict_msg"], dict):
            return json.dumps(self.__dict__["dict_msg"], default=log_encoder)
        else:
            return super().getMessage()
