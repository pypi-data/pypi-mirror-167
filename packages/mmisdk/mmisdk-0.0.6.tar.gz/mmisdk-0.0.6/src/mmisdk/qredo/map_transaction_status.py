def map_transaction_status(status: str, reason: str):
    if (status == 'pending'):
        return {
            "finished": False,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Pending',
            "reason": reason,
        }
    if (status == 'created'):
        return {
            "finished": False,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Created',
            "reason": reason,
        }
    if (status == 'authorized'):
        return {
            "finished": False,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Authorized',
            "reason": reason,
        }
    if (status == 'approved'):
        return {
            "finished": False,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Approved',
            "reason": reason,
        }
    elif (status == 'signed'):
        return {
            "finished": False,
            "submitted": False,
            "signed": True,
            "success": False,
            "displayText": 'Signed',
            "reason": reason,
        }
    elif (status == 'scheduled'):
        return {
            "finished": False,
            "submitted": True,
            "signed": True,
            "success": False,
            "displayText": 'Scheduled',
            "reason": reason,
        }
    elif (status == 'pushed'):
        return {
            "finished": False,
            "submitted": True,
            "signed": True,
            "success": False,
            "displayText": 'Pushed',
            "reason": reason,
        }
    elif (status == 'confirmed'):
        return {
            "finished": False,
            "submitted": True,
            "signed": True,
            "success": False,
            "displayText": 'Confirmed',
            "reason": reason,
        }
    elif (status == 'mined'):
        return {
            "finished": True,
            "submitted": True,
            "signed": True,
            "success": True,
            "displayText": 'Mined',
            "reason": reason,
        }
    elif (status == 'failed'):
        return {
            "finished": True,
            "submitted": True,
            "signed": True,
            "success": False,
            "displayText": 'Failed',
            "reason": reason,
        }
    elif (status == 'expired'):
        return {
            "finished": True,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Aborted',
            "reason": reason,
        }
    elif (status == 'cancelled'):
        return {
            "finished": True,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Cancelled',
            "reason": reason,
        }
    elif (status == 'rejected'):
        return {
            "finished": True,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Rejected',
            "reason": reason,
        }
    else:
        return {
            "finished": False,
            "submitted": False,
            "signed": False,
            "success": False,
            "displayText": 'Unknown',
            "reason": reason,
        }
