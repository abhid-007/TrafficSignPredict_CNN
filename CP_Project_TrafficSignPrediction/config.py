import os
import re
from yacs.config import CfgNode

_C = CfgNode()

_C.GTSRB_ROOT_DIR = 'GTSRB'

_C.TRAIN_ROOT_DIR = os.path.join(_C.GTSRB_ROOT_DIR, 'Final_Training')
_C.TRAIN_PKL_FILENAME = 'traffic_sign_train_dataset.pickle'
_C.TRAIN_SIZE = len([
    f
    for root, dirs, files in os.walk(os.path.join(_C.TRAIN_ROOT_DIR, 'Images'))
    for f in files if re.search(r'.ppm', f)
])

_C.TEST_ROOT_DIR = os.path.join(_C.GTSRB_ROOT_DIR, 'Final_Test')
_C.TEST_PKL_FILENAME = 'traffic_sign_test_dataset.pickle'
_C.TEST_SIZE = len([
    f
    for root, dirs, files in os.walk(os.path.join(_C.TEST_ROOT_DIR, 'Images'))
    for f in files if re.search(r'.ppm', f)
])


def get_default_cfg():
    return _C.clone()
