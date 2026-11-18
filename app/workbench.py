import json
from .committee import proposal
from .journal import packet
from .participation import certify
from .programme import checkpoint, scope


def run_workbench(action, directory, key, ledger):
    if action == 'minute' and key:
        return packet(ledger, 'committee', key)
    source = json.loads((directory / 'workbench.json').read_text())
    period = checkpoint(source['checkpoints'], key or 'spring')
    current_scope = scope(source['activities'], period)
    if action == 'scope':
        return current_scope
    approved = certify(source['proofs'], current_scope, period['date'])
    if action == 'evidence':
        return approved
    candidate = proposal(period, approved)
    return packet(ledger, 'committee', period['id'], candidate) if action == 'minute' else candidate
