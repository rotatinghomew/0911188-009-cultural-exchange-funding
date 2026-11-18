def checkpoint(rows, key):
    row = next((record for record in rows if record['id'] == key), None)
    if not row:
        raise ValueError('找不到该期')
    return row


def scope(activities, period):
    return {row['id']: row['scope'] for row in activities if row['state'] == 'held'
            and period['first_day'] <= row['day'] <= period['date']}
