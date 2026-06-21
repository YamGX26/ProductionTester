from dataclasses import dataclass

@dataclass
class Operator:
    operator_id: str = ""
    shift: str = ""
    model: str = ""