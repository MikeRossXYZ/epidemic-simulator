from constants import HealthStatus


class Entity:
    def __init__(self, name):
        self.name = name
        self.relations = {}
        # Current health status
        self.health_status = HealthStatus.Susceptible
        self.days_at_health_status = 0
        # Current behaviour
        self.behaviour = "Normal"
