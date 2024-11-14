"""
@Time ： 2024-10-27
@Auth ： Adam Lyu
"""
import sqlite3
from typing import Optional

from langchain_core.tools import tool
from utils.logger import logger  # 导入自定义日志记录工具

from scripts.populate_database import db


@tool
def search_trip_recommendations(
        location: Optional[str] = None,
        name: Optional[str] = None,
        keywords: Optional[str] = None,
) -> list[dict]:
    """
    Search for trip recommendations based on location, name, and keywords.
    """
    logger.info("Starting search for trip recommendations.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = "SELECT * FROM trip_recommendations WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if keywords:
        keyword_list = keywords.split(",")
        keyword_conditions = " OR ".join(["keywords LIKE ?" for _ in keyword_list])
        query += f" AND ({keyword_conditions})"
        params.extend([f"%{keyword.strip()}%" for keyword in keyword_list])

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    logger.info(f"Search completed. Found {len(results)} recommendations.")
    return [
        dict(zip([column[0] for column in cursor.description], row)) for row in results
    ]


@tool
def book_excursion(recommendation_id: int) -> str:
    """
    Book an excursion by its recommendation ID.
    """
    logger.info(f"Attempting to book excursion with ID {recommendation_id}.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE trip_recommendations SET booked = 1 WHERE id = ?", (recommendation_id,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        conn.close()
        logger.info(f"Trip recommendation {recommendation_id} successfully booked.")
        return f"Trip recommendation {recommendation_id} successfully booked."
    else:
        conn.close()
        logger.warning(f"No trip recommendation found with ID {recommendation_id}.")
        return f"No trip recommendation found with ID {recommendation_id}."


@tool
def update_excursion(recommendation_id: int, details: str) -> str:
    """
    Update a trip recommendation's details by its ID.
    """
    logger.info(f"Updating details for trip recommendation ID {recommendation_id}.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE trip_recommendations SET details = ? WHERE id = ?",
        (details, recommendation_id),
    )
    conn.commit()

    if cursor.rowcount > 0:
        conn.close()
        logger.info(f"Trip recommendation {recommendation_id} successfully updated.")
        return f"Trip recommendation {recommendation_id} successfully updated."
    else:
        conn.close()
        logger.warning(f"No trip recommendation found with ID {recommendation_id}.")
        return f"No trip recommendation found with ID {recommendation_id}."


@tool
def cancel_excursion(recommendation_id: int) -> str:
    """
    Cancel a trip recommendation by its ID.
    """
    logger.info(f"Attempting to cancel excursion with ID {recommendation_id}.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE trip_recommendations SET booked = 0 WHERE id = ?", (recommendation_id,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        conn.close()
        logger.info(f"Trip recommendation {recommendation_id} successfully cancelled.")
        return f"Trip recommendation {recommendation_id} successfully cancelled."
    else:
        conn.close()
        logger.warning(f"No trip recommendation found with ID {recommendation_id}.")
        return f"No trip recommendation found with ID {recommendation_id}."
