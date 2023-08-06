from datetime import datetime
from optparse import OptionParser
import importlib.util
import pathlib
import logging 

logging.basicConfig(level = logging.INFO)

def parse_options():
    parser = OptionParser()
    parser.add_option('--end_ts', type=int)
    parser.add_option('--dir', type=str)
    parser.add_option('--filename', type=str, default='monitor.py')
    parser.add_option('--methodname', type=str, default='monitor')

    options, _ = parser.parse_args()
    return options


def monitor(dir: str, end_ts: int, filename:str="monitor.py", methodname:str="monitor"):
    """
    Get all files name filename in dir
    for each file:
        execute the method methodname with the end_ts
    :param dir: the directory to scan from
    :param end_ts: the time until it we can monitor
    :param filename: default monitor.py the file name to search in dir
    :param methodname: the methodname name to search in each file. default is monitor
    :return:
    """
    logging.info(
        f"Going to monitor all {filename} files in dir {dir} end ts is {datetime.fromtimestamp(end_ts)}")
    for pyfile in pathlib.Path(dir).glob(f'**/{filename}'):
        try:
            logging.info(f"Going to monitor {pyfile}")
            spec = importlib.util.spec_from_file_location(f"{__name__}.imported_{pyfile.stem}", pyfile)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            monitor_method = getattr(module, methodname)
            res = monitor_method(end_ts)
            logging.info(f"monitor ends with status {res}")
        except Exception as e:
            message = f"Couldn't monitor {pyfile} exception is {e}"
            logging.error(message)
            # you can add slack or email notification

def main(options):
    """
    Get all files name options.filename in options.dir
    for each file:
        execute the method options.methodname with the end_ts
    :param options:
    :return:
    """
    logging.info(f"Going to monitor all {options.filename} files in dir {options.dir} end ts is {datetime.fromtimestamp(options.end_ts)}")
    monitor(options.dir, options.end_ts, options.filename, options.methodname)


if __name__ == '__main__':
    options = parse_options()
    main(options)
