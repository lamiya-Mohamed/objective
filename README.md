====================================================
     OKR Management System
====================================================

                 ┌───────────────────────┐
                 │       System Admin      │
                 │  (Add Orgs / Users)    │
                 └───────────┬───────────┘
                             │
            ┌────────────────▼────────────────┐
            │           Organization            │
            │  - id                             │
            │  - name                           │
            │  - sector                         │
            └───────────┬─────────────────────┘
                        │
          ┌─────────────▼─────────────┐
          │         Objective           │
          │  - name                     │
          │  - owner                    │
          │  - start_date               │
          │  - end_date                 │
          └───────────┬────────────────┘
                      │
        ┌─────────────▼─────────────┐
        │        Key Result           │
        │  - target_value             │
        │  - current_value            │
        │  - weight                   │
        │  - achievement_rate()       │
        └───────────┬────────────────┘
                    │
          ┌─────────▼─────────┐
          │       Task          │
          │  - name             │
          │  - owner            │
          │  - status           │
          │  - due_date         │
          └────────────────────┘


====================================================
 Dashboards & Reports
====================================================

 [ Organization Progress ]
 [ Objective Achievement % ]
 [ Alerts for Delayed Goals ]
 [ Executive Summary View ]
