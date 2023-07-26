from dataclasses import dataclass

@dataclass
class Port:
    containerPort: int
    protocolPort: str
    externalPort: int