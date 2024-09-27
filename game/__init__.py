import logging
from typing import Optional

from game.logger.struct_logger import StructLogRecord

_data_path = None
STRUCT_LOGGER_SET = False
_prefix_path = None
_independent_package: Optional[bool] = None

# Do not raise exceptions during log handling
logging.setLogRecordFactory(StructLogRecord)


def prefix_path() -> str:
    global _prefix_path
    if _prefix_path is None:
        from os.path import join, realpath
        _prefix_path = realpath(join(__file__, "../../"))
    return _prefix_path


def set_prefix_path(p: str):
    global _prefix_path
    _prefix_path = p


def init_logging(conf_filename: str):
    import io
    import logging.config
    from os.path import join, exists
    from os import makedirs
    from typing import Dict

    from ruamel.yaml import YAML

    logs_path: str = join(prefix_path(), "logs")

    if not exists(logs_path):
        makedirs(logs_path, 0o711, exist_ok=True)

    conf_path: str = join(prefix_path(), "conf", conf_filename)
    yaml_parser: YAML = YAML()
    with open(conf_path) as fd:
        yml_source: str = fd.read()
        yml_source = yml_source.replace("$PROJECT_DIR", prefix_path())
        io_stream: io.StringIO = io.StringIO(yml_source)
        config_dict: Dict = yaml_parser.load(io_stream)
        logging.config.dictConfig(config_dict)
