import fastapi
from typing import Optional
from models.location import Location
from fastapi import Depends
from services.openweather_service import get_report
router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    report = await get_report(loc.city, loc.state, loc.country, units)
    return report
