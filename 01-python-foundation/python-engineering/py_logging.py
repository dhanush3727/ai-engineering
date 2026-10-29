# Logging: 
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Task
logger.info("Maintix application started")
logger.warning("Equipment data is missing")
logger.error("Failed to fetch equipment")

# Practical
def summarize_breakdown(equipment_name: str) -> str:
    logger.info("Summarize breakdown for %s", equipment_name)
    if not equipment_name:
        logger.error("Equipment name not found")
        raise ValueError("Equipment name not found")

    return f"Breakdown summary for {equipment_name}"

result = summarize_breakdown("Pump")
print(result)