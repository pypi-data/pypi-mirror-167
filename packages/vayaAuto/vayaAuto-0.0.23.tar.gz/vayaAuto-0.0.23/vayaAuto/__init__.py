
import os
__BASE__ = os.path.abspath('.')


class BaseConfig:
    CONFIGURATION = {}


baseConfig = BaseConfig
from vayaAuto.vayadrive import VayaDrive, VayaException
from vayaAuto.section import Section



