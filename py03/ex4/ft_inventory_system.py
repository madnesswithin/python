#!/usr/bin/env python3
import sys


def parse_inventory(args: list) -> dict:
    inventory = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name, qty_str = parts
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue
        inventory[item_name] = quantity
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item in item_list:
        pct = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {pct}%")

    most_item = item_list[0]
    least_item = item_list[0]
    for item in item_list:
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item
    print(f"Item most abundant: {most_item}"
          f" with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item}"
          f" with quantity {inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
