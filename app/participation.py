from collections import Counter


def certify(proofs, scope, deadline):
    accepted = [row for row in proofs if row['activity'] in scope and row['received'] <= deadline and row['state'] == 'accepted']
    older = {row['supersedes'] for row in accepted}
    latest = [row for row in accepted if row['id'] not in older]
    counts = Counter()
    for row in latest:
        counts[scope[row['activity']]] += row['people']
    return {'counts': dict(counts), 'proofs': [row['id'] for row in latest]}
