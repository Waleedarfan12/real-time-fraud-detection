def check_amount(tx):
    return tx['amount'] > 0

def check_user_id(tx):
    return tx['user_id'] is not None

def check_transaction_type(tx):
    return tx['transaction_type'] in ['payment', 'transfer', 'withdrawal']

def check_timestamp(tx):
    return tx['timestamp'] is not None

def check_device(tx):
    return tx['device'] in ['mobile', 'web', 'ATM']

def check_location(tx):
    return isinstance(tx['location'], str)