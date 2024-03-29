import json

import SharkBot
from discord import Interaction
from discord.app_commands import Choice


SEAL_HASHES: dict[str, str] = {}
root_seal_node = SharkBot.Destiny.Definitions.DestinyPresentationNodeDefinition.get(616318467)
for child_node in root_seal_node["children"]["presentationNodes"]:
    child_node_hash = str(child_node["presentationNodeHash"])
    child_node_definition = SharkBot.Destiny.Definitions.DestinyPresentationNodeDefinition.get(child_node_hash)
    child_seal_name = child_node_definition["displayProperties"]["name"]
    if child_seal_name == "Classified":
        continue
    SEAL_HASHES[child_seal_name] = str(child_node_hash)
    child_completion_record = SharkBot.Destiny.Definitions.DestinyRecordDefinition.get(child_node_definition["completionRecordHash"])
    if child_completion_record["titleInfo"]["hasTitle"]:
        SEAL_HASHES[child_completion_record["titleInfo"]["titlesByGender"]["Male"]] = str(child_node_hash)

PATTERN_SOURCES: list[str] = []
with open("data/static/bungie/definitions/PatternSources.json", "r") as f:
    for sources in json.load(f).values():
        PATTERN_SOURCES.extend(sources)

PATTERN_SOURCES = list(set(PATTERN_SOURCES))

def items_to_choices(items: list[SharkBot.Item.Item]) -> list[Choice]:
    return [
        Choice(
            name=f"[{item.id}] {item.name}",
            value=item.id
        ) for item in list(set(items))[0:25]
    ]

def balance_to_choices(numbers: list[int]) -> list[Choice]:
    return [
        Choice(
            name=f"${number}",
            value=number
        ) for number in numbers
    ]

class Autocomplete:

    @staticmethod
    async def inventory_item(interaction: Interaction, current: str):
        member = SharkBot.Member.get(interaction.user.id, create=False)
        return items_to_choices(
            member.inventory.filter(lambda i: SharkBot.Utils.item_contains(i, current.lower()))
        )

    @staticmethod
    async def member_discovered_item(interaction: Interaction, current: str):
        member = SharkBot.Member.get(interaction.user.id, create=False)
        return items_to_choices(
            [item for item in member.collection.items if SharkBot.Utils.item_contains(item, current.lower())]
        )

    @staticmethod
    async def openable_item(interaction: Interaction, current: str):
        member = SharkBot.Member.get(interaction.user.id, create=False)
        return items_to_choices(
            [item for item in member.inventory.filter(lambda i: i.openable) if SharkBot.Utils.item_contains(item, current.lower())]
        )

    @staticmethod
    async def member_balance(interaction: Interaction, current: str) -> list[Choice]:
        member = SharkBot.Member.get(interaction.user.id, create=False)
        try:
            current = int(current)
        except ValueError:
            return [
                Choice(
                    name=f"${member.balance} - Balance",
                    value=member.balance
                )
            ]
        if current >= member.balance:
            return [
                Choice(
                    name=f"You don't have ${current}!",
                    value=current
                ),
                Choice(
                    name=f"${member.balance} - Balance",
                    value=member.balance
                )
            ]
        else:
            tens = []
            i = current * 10
            while i < member.balance:
                tens.append(i)
                i *= 10
            return [
                Choice(
                    name=f"${current}",
                    value=current
                )
            ] + balance_to_choices(tens)[0:3] + [
                Choice(
                    name=f"${member.balance} - Balance",
                    value=member.balance
                )
            ]

    @staticmethod
    async def shop_items(interaction: Interaction, current: str) -> list[Choice]:
        current = current.lower()
        results = []
        try:
            for listing in SharkBot.Listing.listings:
                if SharkBot.Utils.item_contains(listing.item, current):
                    results.append(
                        Choice(
                            name=f"{listing.item.name} - ${listing.price}",
                            value=listing.item.id
                        )
                    )
            return results
        except Exception as e:
            print(e)

    @staticmethod
    async def seal(interaction: Interaction, current: str) -> list[Choice]:
        current = current.lower()
        return [
            Choice(
                name=seal_name,
                value=seal_hash
            ) for seal_name, seal_hash in SEAL_HASHES.items() if current in seal_name.lower()
        ][0:10]

    @staticmethod
    async def destiny_definition(interaction: Interaction, current: str) -> list[Choice]:
        current = current.lower()
        return [
            Choice(
                name=full_definition,
                value=sub_definition
            ) for sub_definition, full_definition in SharkBot.Destiny.Manifest.DEFINITIONS_LOOKUP.items() if current in sub_definition
        ][0:10]

    @staticmethod
    async def pattern_source(interaction: Interaction, current: str) -> list[Choice]:
        current = current.lower()
        return [
            Choice(
                name=source,
                value=source
            ) for source in PATTERN_SOURCES if current in source.lower()
        ][0:10]
