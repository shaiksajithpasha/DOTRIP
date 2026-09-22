import enum

class Role(str, enum.Enum):
    RIDER = "RIDER"
    VENDOR = "VENDOR"
    DRIVER = "DRIVER"
    ADMIN = "ADMIN"
    SUPPORT_AGENT = "SUPPORT_AGENT"
    SUPER_ADMIN = "SUPER_ADMIN"

class AddressType(str, enum.Enum):
    HOME = "HOME"
    OFFICE = "OFFICE"
    OTHER = "OTHER"
    PICKUP = "PICKUP"
    DROP = "DROP"

class MessageStatus(str, enum.Enum):
    READ = "READ"
    UNREAD = "UNREAD"
