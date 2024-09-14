from pydantic import BaseModel

class MiningUser(BaseModel):
    user_name: int
    email: str
