"""Pydantic schemas for Last-Mile Delivery Batching."""

from typing import List
from pydantic import BaseModel, Field


class DeliveryBatch(BaseModel):
    """Structured delivery batch assigned to an individual two-wheeler delivery rider."""

    batch_id: str = Field(
        description="Unique identifier for the dispatch batch (e.g., 'BATCH-01', 'BATCH-02')"
    )
    assigned_orders: List[str] = Field(
        description="List of order IDs grouped into this delivery run (e.g., ['ORD-101', 'ORD-104'])"
    )
    total_weight_kg: float = Field(
        description="Sum of item weights across all pooled orders in kilograms (strictly <= 15.0 kg)"
    )
    estimated_route_time_mins: int = Field(
        description="Estimated total round-trip delivery circuit duration in minutes from Dark Store (0,0) through all customer stops"
    )
    route_rationale: str = Field(
        description="Logistical explanation detailing spatial proximity, shared delivery corridor, rider weight safety, and SLA prioritization"
    )


class BatchingPlan(BaseModel):
    """Comprehensive multi-batch dispatch plan covering all incoming orders."""

    plan_id: str = Field(
        description="Dispatch plan identifier"
    )
    batches: List[DeliveryBatch] = Field(
        description="List of optimized delivery batches assigned to individual riders"
    )
    total_orders_batched: int = Field(
        description="Total count of customer orders assigned across all batches"
    )
    total_riders_required: int = Field(
        description="Number of two-wheeler delivery riders required to fulfill the dispatch plan"
    )
    fleet_dispatch_summary: str = Field(
        description="Executive summary of fleet capacity utilization and SLA adherence"
    )
