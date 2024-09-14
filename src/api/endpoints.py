from fastapi import APIRouter, HTTPException
from core.referral_utils import generate_referral_code
import asyncio

router = APIRouter()

@router.get("/generate_referral_code")
async def referral_code_generation():
    return generate_referral_code()
