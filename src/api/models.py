from pydantic import BaseModel

class MiningUser(BaseModel):
    user_name: str
    email: str


class UserReferral(BaseModel):
    user_name: str
    referral_code: str
