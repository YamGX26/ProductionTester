from dataclasses import dataclass

@dataclass
class Settings:
    test_mode: str = "Development"
    com_port: str = "COM1"
    log_path: str = "./logs"