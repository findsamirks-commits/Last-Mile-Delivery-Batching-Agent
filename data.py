"""Synthetic order feed and spatial grid data for a quick-commerce micro-fulfillment center (Dark Store).
All customer orders are located within a 5km radius of the Dark Store at coordinate (0, 0).
"""

import math
from typing import Any, Dict, List, Tuple
import pandas as pd

DARK_STORE_COORDS: Tuple[float, float] = (0.0, 0.0)
DARK_STORE_ID = "MFC-BLR-KORAMANGALA-01"

# 10 realistic quick-commerce orders distributed across directional radial corridors
SYNTHETIC_ORDERS: List[Dict[str, Any]] = [
    {
        "order_id": "ORD-101",
        "customer_name": "Aarav Sharma",
        "address": "4th Block, 100ft Road",
        "x_km": 1.2,
        "y_km": 1.8,
        "weight_kg": 3.8,
        "sla_deadline": "10 mins",
        "sla_mins": 10,
        "items_summary": "Milk, Fresh Bread, Eggs",
    },
    {
        "order_id": "ORD-102",
        "customer_name": "Priya Nair",
        "address": "5th Block, 80ft Road",
        "x_km": 1.5,
        "y_km": 2.1,
        "weight_kg": 4.5,
        "sla_deadline": "10 mins",
        "sla_mins": 10,
        "items_summary": "Paneer, Curd, Vegetables",
    },
    {
        "order_id": "ORD-103",
        "customer_name": "Rohan Mehta",
        "address": "1st Block Extension",
        "x_km": 0.9,
        "y_km": 2.5,
        "weight_kg": 5.2,
        "sla_deadline": "20 mins",
        "sla_mins": 20,
        "items_summary": "Atta 5kg, Cooking Oil 1L",
    },
    {
        "order_id": "ORD-104",
        "customer_name": "Sneha Reddy",
        "address": "Ejipura Main Road",
        "x_km": -1.8,
        "y_km": 1.4,
        "weight_kg": 2.8,
        "sla_deadline": "10 mins",
        "sla_mins": 10,
        "items_summary": "Ice Cream Tub, Chocolates",
    },
    {
        "order_id": "ORD-105",
        "customer_name": "Vikram Sen",
        "address": "Vivek Nagar Cross",
        "x_km": -2.2,
        "y_km": 1.9,
        "weight_kg": 3.4,
        "sla_deadline": "20 mins",
        "sla_mins": 20,
        "items_summary": "Soft Drinks 2L, Chips, Dips",
    },
    {
        "order_id": "ORD-106",
        "customer_name": "Ananya Joshi",
        "address": "National Games Village",
        "x_km": -1.4,
        "y_km": 0.8,
        "weight_kg": 4.1,
        "sla_deadline": "10 mins",
        "sla_mins": 10,
        "items_summary": "Fresh Chicken, Spices",
    },
    {
        "order_id": "ORD-107",
        "customer_name": "Karan Malhotra",
        "address": "Tavarekere Park View",
        "x_km": 0.3,
        "y_km": -2.1,
        "weight_kg": 3.2,
        "sla_deadline": "10 mins",
        "sla_mins": 10,
        "items_summary": "Coffee Powder, Oats, Berries",
    },
    {
        "order_id": "ORD-108",
        "customer_name": "Meera Iyer",
        "address": "BTM 1st Stage",
        "x_km": 0.6,
        "y_km": -2.6,
        "weight_kg": 4.0,
        "sla_deadline": "20 mins",
        "sla_mins": 20,
        "items_summary": "Basmati Rice 3kg, Ghee",
    },
    {
        "order_id": "ORD-109",
        "customer_name": "Aditya Verma",
        "address": "HSR Layout Sector 5",
        "x_km": 2.8,
        "y_km": -1.1,
        "weight_kg": 3.6,
        "sla_deadline": "10 mins",
        "sla_mins": 10,
        "items_summary": "Fruits Basket, Greek Yogurt",
    },
    {
        "order_id": "ORD-110",
        "customer_name": "Divya Patel",
        "address": "HSR Layout Sector 4",
        "x_km": 3.1,
        "y_km": -1.4,
        "weight_kg": 4.2,
        "sla_deadline": "20 mins",
        "sla_mins": 20,
        "items_summary": "Detergent Liquid, Fabric Softener",
    },
]


def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate straight-line Euclidean distance in kilometers between two spatial coordinates."""
    return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2), 2)


def get_dark_store_coords() -> Tuple[float, float]:
    """Return coordinates of the fulfillment hub."""
    return DARK_STORE_COORDS


def get_orders() -> List[Dict[str, Any]]:
    """Return synthetic order records with computed distance from dark store."""
    orders = []
    for item in SYNTHETIC_ORDERS:
        order = item.copy()
        order["dist_from_hub_km"] = calculate_distance(DARK_STORE_COORDS, (order["x_km"], order["y_km"]))
        orders.append(order)
    return orders


def get_orders_df() -> pd.DataFrame:
    """Return order records structured as a pandas DataFrame."""
    return pd.DataFrame(get_orders())


if __name__ == "__main__":
    df = get_orders_df()
    print("Dark Store Location:", DARK_STORE_COORDS)
    print("Incoming Quick-Commerce Orders (10 stops within 5km radius):")
    print(df[["order_id", "customer_name", "x_km", "y_km", "dist_from_hub_km", "weight_kg", "sla_deadline"]])
