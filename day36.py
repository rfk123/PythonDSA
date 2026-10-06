

class CreditPools:
    def __init__(self):
        self.pool = {}  # {pool_id: credits}
        self.spending = {}  # {pool: amount_spent cumulative}
        self.holds = {}  # { hold_id: (pool_id, amount, expires_at)}
        self.time = 0

    def create_pool(self, pool_id: str, credits: int) -> bool:
        if pool_id in self.pool or credits < 0:
            return False
        self.pool[pool_id] = credits
        self.spending[pool_id] = 0
        return True

    def get_balance(self, pool_id: str) -> int | None:
        if pool_id not in self.pool:
            return None
        return self.pool[pool_id]

    def add_credits(self, pool_id: str, amount: int) -> bool:
        if pool_id not in self.pool or amount <= 0:
            return False
        self.pool[pool_id] += amount
        return True

    def spend(self, pool_id: str, amount: int) -> bool:
        if pool_id not in self.pool or amount <= 0 or self.get_available(pool_id) < amount:
            return False
        self.pool[pool_id] -= amount
        self.spending[pool_id] += amount
        return True

    def transfer(self, source_id: str, target_id: str, amount: int) -> bool:
        if source_id not in self.pool or target_id not in self.pool or source_id == target_id or amount <= 0 or self.get_available(source_id) < amount:
            return False
        self.pool[source_id] -= amount
        self.pool[target_id] += amount
        return True

    def top_spenders(self, limit: int) -> list[str]:
        if limit <= 0:
            return []
        spenders = sorted(self.spending, key=lambda pool: (
            -self.spending[pool], pool))
        return spenders[:limit]

    def advance_time(self, now: int) -> bool:
        if now < self.time:
            return False
        self.time = now
        for hold, pool_info in list(self.holds.items()):
            if pool_info[2] <= self.time:
                del self.holds[hold]
        return True

    def hold(self, hold_id: str, pool_id: str, amount: int, expires_at: int) -> bool:
        if hold_id in self.holds or pool_id not in self.pool or amount <= 0 or self.pool[pool_id] < amount or expires_at <= self.time:
            return False
        available = self.get_available(pool_id)
        if available < amount:
            return False
        self.holds[hold_id] = (pool_id, amount, expires_at)
        return True

    def get_available(self, pool_id: str) -> int | None:
        if pool_id not in self.pool:
            return None
        held = 0
        for hold in self.holds.values():
            if hold[0] == pool_id:
                held += hold[1]

        return self.pool[pool_id] - held

    def release_hold(self, hold_id: str) -> bool:
        if hold_id not in self.holds:
            return False
        del self.holds[hold_id]
        return True

    def capture_hold(self, hold_id: str) -> bool:
        if hold_id not in self.holds:
            return False
        hold = self.holds[hold_id]
        self.spending[hold[0]] += hold[1]
        self.pool[hold[0]] -= hold[1]
        del self.holds[hold_id]
        return True

    def merge_pools(self, source_id: str, target_id: str) -> bool:
        if source_id not in self.pool or target_id not in self.pool or source_id == target_id:
            return False
        self.pool[target_id] += self.pool[source_id]
        for hold, pool_info in list(self.holds.items()):
            if pool_info[0] == source_id:
                self.holds[hold] = (target_id, pool_info[1], pool_info[2])
        self.spending[target_id] += self.spending[source_id]
        del self.spending[source_id]
        del self.pool[source_id]
        return True


# Test Level 1
# system = CreditPools()
# assert system.create_pool("alpha", 10)
# assert system.create_pool("alpha", 20) is False
# assert system.spend("alpha", 11) is False
# assert system.spend("alpha", 4)
# assert system.get_balance("alpha") == 6
# assert system.get_balance("missing") is None
# successful tets, 1 hour and 22 minutes more to go


# Test Level 2
# system = CreditPools()
# system.create_pool("b", 10)
# system.create_pool("a", 10)
# system.create_pool("c", 10)

# assert system.spend("b", 3)
# assert system.spend("a", 3)
# assert system.transfer("c", "b", 5)
# assert system.top_spenders(3) == ["a", "b", "c"]
# assert system.get_balance("b") == 12
# Successful tests, 1 hour and 11 minutes more to go
# Had an issue where I was sorting the top spenders in ascending order and not descending

# Test Level 3
# system = CreditPools()
# system.create_pool("alpha", 10)

# assert system.hold("h1", "alpha", 6, 5)
# assert system.get_balance("alpha") == 10
# assert system.get_available("alpha") == 4
# assert system.spend("alpha", 5) is False

# assert system.advance_time(4)
# assert system.get_available("alpha") == 4
# assert system.advance_time(5)
# assert system.get_available("alpha") == 10
# assert system.capture_hold("h1") is False

# assert system.hold("h1", "alpha", 3, 8)
# assert system.capture_hold("h1")
# assert system.get_balance("alpha") == 7
# assert system.get_available("alpha") == 7
# tests passed for level 3 after I ran into trouble deleting dictionary elements while looping through a dictionary in advance time and I also had to change the way I kept track of holds
# so that the balanace for the pool never changes unless there is a spend or a hold is captured. Finished with 24 minutes remaining.

# Test Level 4
system = CreditPools()
system.create_pool("source", 10)
system.create_pool("target", 5)
system.spend("source", 2)
system.hold("h1", "source", 3, 10)
system.hold("h2", "target", 2, 10)

assert system.merge_pools("source", "target")
assert system.get_balance("source") is None
assert system.get_balance("target") == 13
assert system.get_available("target") == 8

assert system.capture_hold("h1")
assert system.get_balance("target") == 10
assert system.get_available("target") == 8

assert system.create_pool("source", 0)
assert system.top_spenders(2) == ["target", "source"]

assert system.advance_time(10)
assert system.get_available("target") == 10
# Level 4 Test was passed in the first try with now 16 minutes left to go
