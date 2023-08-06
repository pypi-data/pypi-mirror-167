import logging
import subprocess
import inspect
import os

logger = logging.getLogger(__name__)

# Just simulating an RCE bug in Tienda, where we use an imaginary third party library "CheckPhone" to do some sort of
# phone number validation. This bug is of the simplest possible kind, user input passed to subprocess


def check_it(mobile_number: str):
    logger.info(f"I am checking: {mobile_number}")
    if len(mobile_number) >= 8:
        try:
            my_dir = os.path.dirname(inspect.getfile(check_it))

            subprocess.check_output(f"{my_dir}/libs/checkphone {mobile_number}", shell=True)
        except subprocess.CalledProcessError:
            return False
        return True
