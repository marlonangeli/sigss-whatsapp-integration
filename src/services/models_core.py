import os
import sys
path = os.path.abspath(os.getcwd())
sys.path.append(path)

from src.models.material import *
from src.models.paciente import *
from src.models.whatsapp import *
from src.models.emprestimo import *
