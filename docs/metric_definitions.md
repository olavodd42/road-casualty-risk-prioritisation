# Metric definitions

These KPI definitions standardise the numerator, denominator, unit, and
aggregation rules used in analysis and dashboard outputs. Casualty counts
refer to people injured or killed, while collision counts refer to recorded
collision events.

| KPI | Formula | Unit and rules |
| --- | --- | --- |
| Collisions | `count(distinct collision_id)` | Count. Always by collision, never by joined rows. |
| Casualties | `count(*)` in casualty fact | Count. |
| KSI casualties | Casualties with severity ∈ {fatal, serious} | Count. Verify codes in the data guide. |
| KSI share | KSI casualties ÷ total casualties | %. Aggregate numerator and denominator first, then divide. Never average percentages. |
| Collision severity rate | Collisions with ≥1 fatal/serious casualty ÷ collisions | %. |
| Casualties per collision | Casualties ÷ collisions | Ratio. |
| Vulnerable road user (VRU) KSI share | KSI among pedestrians, pedal cyclists and motorcyclists ÷ all KSI | %. Define the casualty-type mapping in a dbt seed. |
| Dark-hours share | Collisions in darkness ÷ collisions | %. Based on the light-conditions code. |
