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
PRODUCT_TYPES = [
    ('ELECTRONICS', 'Electronics'),
    ('FURNITURE', 'Furniture'),
    ('CLOTHING', 'Clothing'),
    ('FOOD', 'Food'),
    ('TOYS', 'Toys'),
    ('BOOKS', 'Books'),
    ('BEAUTY', 'Beauty'),
    ('SPORTS', 'Sports'),
    ('JEWELRY', 'Jewelry'),
    ('AUTOMOTIVE', 'Automotive'),
    ('HEALTH', 'Health'),
    ('GARDEN', 'Garden'),
    ('MUSICAL_INSTRUMENTS', 'Musical Instruments'),
    ('OFFICE_SUPPLIES', 'Office Supplies'),
    ('PET_SUPPLIES', 'Pet Supplies'),
    ('TOOLS', 'Tools'),
    ('OTHER', 'Other'),
]