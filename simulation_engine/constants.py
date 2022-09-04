import enum


class HealthStatus(enum.Enum):
    Susceptible = enum.auto()
    Infected = enum.auto()
    Resolved = enum.auto()
