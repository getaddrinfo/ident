from dataclasses import dataclass

@dataclass
class Application:
    id: int
    name: str

@dataclass
class PolicyExecutionResult:
    allow: bool
    