from pydantic_practice import Example
from datetime import datetime


try:
    Example(
        name="    ",
        count=50,
        status="open",
        created_at=datetime.now()
    )
except Exception as e:
    print(e)