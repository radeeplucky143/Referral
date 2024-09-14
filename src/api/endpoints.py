from fastapi import APIRouter, HTTPException
import asyncio

router = APIRouter()

@router.get("/generate_referral_code")
async def generate_referral_code():
    return "S7BHG9"
