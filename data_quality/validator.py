from data_quality.checks import *

def validate_transaction(tx):
    checks = [
        check_amount(tx),
        check_user_id(tx),
        check_transaction_type(tx),
        check_timestamp(tx),
        check_device(tx),
        check_location(tx)
    ]

    return all(checks)