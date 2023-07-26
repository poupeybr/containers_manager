from dataclasses import dataclass
from typing import List
from app.models.environmentVariable import EnvironmentVariable

from app.models.port import Port
from app.models.volume import Volume

@dataclass
class Container:
    containerName: str = None
    image: str = None
    ports: List[Port] = None
    environmentVariables: List[EnvironmentVariable] = None
    volumes: List[Volume] = None
    network: str = None
    ip: str = None
    restartPolicy: str = None