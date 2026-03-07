# models/enums/enums.py
import enum

class TableNames(enum.Enum):
    USERS = "users"
    URLS = "urls"
    CLICK_EVENTS = "click_events"