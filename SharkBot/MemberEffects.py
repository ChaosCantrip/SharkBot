from datetime import datetime, timedelta
from typing import TypedDict, Optional, Union

_EXPIRY_FORMAT = "%d/%m/%Y-%H:%M:%S"

from SharkBot.Errors import Effects as Errors
from SharkBot import Utils

class _MemberEffectData(TypedDict):
    effect_id: str
    expiry: Optional[str]
    charges: Optional[int]


class _MemberEffect:

    def __init__(self, effect_id: str, expiry: Optional[Union[str, datetime]] = None, charges: Optional[int] = None):
        if type(expiry) == str:
            expiry = datetime.strptime(expiry, _EXPIRY_FORMAT)
        self.id = effect_id
        self._expiry = expiry
        self._charges = charges
        self.icon = _icons.get(effect_id, ":question:")

    @property
    def expiry(self) -> Optional[datetime]:
        return self._expiry

    @expiry.setter
    def expiry(self, value: datetime):
        self._expiry = value

    @property
    def charges(self) -> Optional[int]:
        return self._charges

    @charges.setter
    def charges(self, value: int):
        self._charges = value

    @property
    def expired(self) -> bool:
        if self._charges is not None:
            return self._charges <= 0
        elif self._expiry is not None:
            return self._expiry < datetime.utcnow()
        else:
            raise Errors.InvalidEffectDataError(self.data)

    @property
    def _expiry_data(self) -> Optional[str]:
        if self._expiry is None:
            return None
        else:
            return datetime.strftime(self._expiry, _EXPIRY_FORMAT)

    @property
    def data(self) -> _MemberEffectData:
        return {
            "effect_id": self.id,
            "expiry": self._expiry_data,
            "charges": self._charges
        }

    @property
    def db_data(self) -> dict[str, str | int]:
        return {
            "name": self.id,
            "expiry": None if self._expiry is None else int(self._expiry.timestamp() * 1000),
            "charges": self._charges
        }

    @property
    def details(self) -> str:
        output = []
        if self.charges is not None:
            output.append(f"Charges: `{self.charges}`")
        if self.expiry is not None:
            td = self.expiry - datetime.utcnow()
            output.append(f"Expires in: `{Utils.td_to_string(td)}`")
        return "\n".join(output)


class MemberEffects:

    def __init__(self, member_data: list[_MemberEffectData]):
        self._effects: list[_MemberEffect] = [_MemberEffect(**effect_data) for effect_data in member_data]

    def __contains__(self, item):
        self.effect_is_active(item)

    def remove_expired(self):
        for effect in self._effects:
            if effect.expired:
                self._effects.remove(effect)

    def get(self, effect_id: str) -> Optional[_MemberEffect]:
        for effect in self._effects:
            if effect.id == effect_id:
                if effect.expired:
                    self._effects.remove(effect)
                    return None
                else:
                    return effect
        else:
            return None

    def effect_is_active(self, effect_id: str) -> bool:
        return self.get(effect_id) is not None

    def add(self, effect_id: str, charges: Optional[int] = None, expiry: Optional[timedelta] = None, sub_effects: Optional[list[str]] = None, super_effects: Optional[list[str]] = None):
        effect = self.get(effect_id)
        if effect is None:
            effect = _MemberEffect(
                effect_id=effect_id,
                charges=charges,
                expiry=(datetime.utcnow() + expiry) if expiry is not None else None
            )
            self._effects.append(effect)
        else:
            if expiry is not None:
                effect.expiry += expiry
            if charges is not None:
                effect.charges += charges

        if super_effects is not None and expiry is not None:
            for effect_id in super_effects:
                super_effect = self.get(effect_id)
                if super_effect is not None:
                    time_remaining = super_effect.expiry - datetime.utcnow()
                    effect.expiry += time_remaining

        if sub_effects is not None and expiry is not None:
            for effect_id in sub_effects:
                effect = self.get(effect_id)
                if effect is not None:
                    effect.expiry += expiry


    def use_charge(self, effect_id: str, num: int = 1):
        effect = self.get(effect_id)
        if effect is None:
            raise Errors.EffectNotActiveError(effect_id)
        if effect.charges is None:
            raise Errors.EffectDoesNotHaveChargesError(effect_id)
        if effect.charges < num:
            raise Errors.NotEnoughChargesError(effect_id)
        effect.charges -= num
        if effect.charges <= 0:
            self._effects.remove(effect)

    @property
    def data(self) -> list[_MemberEffectData]:
        self.remove_expired()
        return [effect.data for effect in self._effects]

    @property
    def db_data(self):
        self.remove_expired()
        return [effect.db_data for effect in self._effects]

    @property
    def details(self) -> list[list[str, str]]:
        output = []
        overclockers = []
        for effect in self._effects:
            if effect.id.startswith("Overclocker"):
                overclockers.append([f"{effect.icon} {effect.id}", effect.details])
            else:
                output.append([f"{effect.icon} {effect.id}", effect.details])
        if len(overclockers) > 0:
            overclockers.sort(key=lambda x: overclocker_order.index(" ".join(x[0].split(" ")[1:])))
            for overclocker in overclockers[1:]:
                overclocker[0] += " `paused`"
            output.extend(overclockers)
        return output

overclocker_order = [
    "Overclocker (Ultimate)",
    "Overclocker (Huge)",
    "Overclocker (Large)",
    "Overclocker (Medium)",
    "Overclocker (Small)"
]

_icons = {
    "Loaded Dice": ":game_die:",
    "Lucky Clover": ":four_leaf_clover:",
    "Binder": ":blue_book:",
    "God's Binder": ":closed_book:",
    "XP Elixir": ":test_tube:",
    "Money Bag": ":moneybag:",
    "Overclocker (Small)": ":battery:",
    "Overclocker (Medium)": ":battery:",
    "Overclocker (Large)": ":battery:",
    "Overclocker (Huge)": ":battery:",
    "Overclocker (Ultimate)": ":battery:",
    "Counting Charm": ":military_medal:"
}