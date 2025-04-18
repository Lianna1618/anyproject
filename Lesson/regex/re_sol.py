# Create a simple config file parser.
# Config file has the following syntax:
# Comments begin with # (may be in the beginning of the line or in the middle of the line.
# Blank lines are allowed.
# Format of string is key = value
# Spaces are allowed around assignment. 

# Expected output: The data must be loaded into dictionary.
# NOTE: Use logging in solution

import logging
import re

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="my_log.log",
    filemode="w+",
    encoding="utf-8",
)


def get_data_from_file(filename):

    try:
        with open(filename, "r+") as f:
            data = f.read()
            pattern = r"\w+\s\=\s\d+"
            res = re.findall(pattern, data)
            logging.info(f"{filename} file is opened")
            return res
    except Exception as e:
        logging.error(e)


full_data = get_data_from_file("config_file.txt")
my_dict = {}
for data in full_data:
    key, value = data.split("=")
    my_dict[key.strip()] = value.strip()
print(my_dict)
