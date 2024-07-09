class RewardResponse:

    def __init__(self, reward_type: str, reward_amount: int):
        self.reward_type: str = reward_type
        self.reward_amount: int = reward_amount
