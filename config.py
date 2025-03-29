import datetime
VENDOR = 'vendor'
CUSTOMER = 'user'
STAFF = 'staff'

ROLE_CHOICES = [
    ('VENDOR', 'Vendor'),
    ('CUSTOMER', 'Customer'),
    ('STAFF', 'Staff'),
]


FREE = 'Free'
BASIC = 'Basic'
PREMIUM  = 'Premium'
PLAN_CHOICES = [
        ("free", "Free"),
        ("basic", "Basic"),
        ("premium", "Premium"),
    ]