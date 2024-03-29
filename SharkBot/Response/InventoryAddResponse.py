import SharkBot


class InventoryAddResponse:

    def __init__(self, item: SharkBot.Item.Item = None, new_item: bool = False, auto_vault: bool = False, clover_used: bool = False, dice_used: bool = False, charm_used: bool = False):
        self.item = item
        self.new_item = new_item
        self.auto_vault = auto_vault
        self.clover_used = clover_used
        self.dice_used = dice_used
        self.charm_used = charm_used

    @property
    def raw_flags(self) -> list[str]:
        _flags = []
        if self.new_item:
            _flags.append("new_item")
        if self.auto_vault:
            _flags.append("auto_vault")
        if self.clover_used:
            _flags.append("clover_used")
        if self.dice_used:
            _flags.append("dice_used")
        if self.charm_used:
            _flags.append("charm_used")
        return _flags

    @property
    def flags(self) -> list[str]:
        _flags = []
        if self.new_item:
            _flags.append(":sparkles:")
        if self.auto_vault:
            _flags.append(":gear:")
        if self.clover_used:
            _flags.append(":four_leaf_clover:")
        if self.dice_used:
            _flags.append(":game_die:")
        if self.charm_used:
            _flags.append(":military_medal:")
        return _flags

    @property
    def item_printout(self) -> str:
        return str(self.item) + " " + " ".join(self.flags)

    def __str__(self) -> str:
        return self.item_printout
