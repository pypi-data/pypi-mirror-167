import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)

if True:
    from alphafed.examples.fed_avg.demos import (AGGREGATOR_ID, get_scheduler,
                                                 get_task_id)

task_id = get_task_id()
scheduler = get_scheduler()
scheduler._setup_context(id=AGGREGATOR_ID, task_id=task_id, is_initiator=True)
for _ in scheduler.contractor.contract_events():
    print('clean 1 msg')
