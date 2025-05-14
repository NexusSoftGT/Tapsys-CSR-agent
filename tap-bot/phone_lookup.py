# ✅ Simulated Database of Merchants
MERCHANTS = {
    "03212430237": {"name": "Karim", "salutation": "Saheb"},
    "03000222922": {"name": "Fouzia", "salutation": "Saheba"},
    "03330220803": {"name": "Sohaib", "salutation": "Saheb"}
}

def get_merchant(phone_number):
    """Find merchant by phone number"""
    return MERCHANTS.get(phone_number, None)
