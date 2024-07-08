class Lootpool:
    
    def __init__(self, id: str, rewards: list[dict]):
        self.id: str = id
        self._rewards: list[dict] = rewards
