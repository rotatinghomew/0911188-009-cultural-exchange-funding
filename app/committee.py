def proposal(period, certificate):
    missing = {key: threshold - certificate['counts'].get(key, 0) for key, threshold in period['expected'].items()
               if certificate['counts'].get(key, 0) < threshold}
    return {'checkpoint': period['id'], 'shortfall': missing, 'amount': 0 if missing else period['amount'], **certificate}
