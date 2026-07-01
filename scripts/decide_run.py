#!/usr/bin/env python3
"""
Decides whether today's practice run should happen.
Weekdays: ~95% chance to run.
Weekends (Sat/Sun): ~30% chance to run (so weekends are mostly, not always, skipped).

Writes "run=true" or "run=false" to the GITHUB_OUTPUT file so the workflow
can branch on it.
"""

import datetime
import os
import random

today = datetime.date.today()
is_weekend = today.weekday() >= 5  # 5 = Saturday, 6 = Sunday

run_today = random.random() < (0.30 if is_weekend else 0.95)

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"run={'true' if run_today else 'false'}\n")

print(f"Weekend: {is_weekend}, running today: {run_today}")
