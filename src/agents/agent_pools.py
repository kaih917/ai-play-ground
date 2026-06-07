class AgentPool:
    max_capacity: int
    pool_capacity: int
    full_status: bool
    available: int

    def __init__(self, max_capacity: int, pool_capacity: int):
        self.max_capacity = max_capacity
        self.pool_capacity = pool_capacity
        self.full_status = False
        self.available = self.max_capacity