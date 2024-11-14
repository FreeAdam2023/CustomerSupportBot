"""
@Time ： 2024-10-27
@Auth ： Adam Lyu
"""
import sqlite3
from datetime import datetime, date
from typing import Optional, Union
from langchain_core.tools import tool
from scripts.populate_database import db
from utils.logger import logger


@tool
def search_hotels(
        location: Optional[str] = None,
        name: Optional[str] = None,
        price_tier: Optional[str] = None,
        checkin_date: Optional[Union[datetime, date]] = None,
        checkout_date: Optional[Union[datetime, date]] = None,
) -> list[dict]:
    """
    Search for hotels based on location, name, price tier, check-in date, and check-out date.
    """
    logger.info("Starting search_hotels with parameters.")
    logger.debug(f"Parameters: location={location}, name={name}, price_tier={price_tier}, "
                 f"checkin_date={checkin_date}, checkout_date={checkout_date}")

    query = "SELECT * FROM hotels WHERE 1=1"
    params = []
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if price_tier:
        query += " AND price_tier = ?"
        params.append(price_tier)

    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            logger.debug(f"Executing query: {query} with params: {params}")
            cursor.execute(query, params)
            results = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            logger.info(f"search_hotels found {len(results)} results.")
    except Exception as e:
        logger.error(f"Database error during search_hotels: {e}")
        return []

    return [dict(zip(columns, row)) for row in results]


@tool
def book_hotel(hotel_id: int) -> str:
    """
    Book a hotel by its ID.
    """
    logger.info(f"Attempting to book hotel with ID {hotel_id}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("UPDATE hotels SET booked = 1 WHERE id = ?", (hotel_id,))
    conn.commit()

    if cursor.rowcount > 0:
        logger.info(f"Hotel {hotel_id} successfully booked.")
        conn.close()
        return f"Hotel {hotel_id} successfully booked."
    else:
        logger.warning(f"No hotel found with ID {hotel_id}.")
        conn.close()
        return f"No hotel found with ID {hotel_id}."


@tool
def update_hotel(
    hotel_id: int,
    checkin_date: Optional[Union[datetime, date]] = None,
    checkout_date: Optional[Union[datetime, date]] = None,
) -> str:
    """
    Update a hotel's check-in and check-out dates by its ID.
    """
    logger.info(f"Updating hotel {hotel_id} with new dates.")
    logger.debug(f"New dates: checkin_date={checkin_date}, checkout_date={checkout_date}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    if checkin_date:
        cursor.execute("UPDATE hotels SET checkin_date = ? WHERE id = ?", (checkin_date, hotel_id))
    if checkout_date:
        cursor.execute("UPDATE hotels SET checkout_date = ? WHERE id = ?", (checkout_date, hotel_id))

    conn.commit()

    if cursor.rowcount > 0:
        logger.info(f"Hotel {hotel_id} successfully updated.")
        conn.close()
        return f"Hotel {hotel_id} successfully updated."
    else:
        logger.warning(f"No hotel found with ID {hotel_id}.")
        conn.close()
        return f"No hotel found with ID {hotel_id}."


@tool
def cancel_hotel(hotel_id: int) -> str:
    """
    Cancel a hotel by its ID.
    """
    logger.info(f"Attempting to cancel hotel with ID {hotel_id}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("UPDATE hotels SET booked = 0 WHERE id = ?", (hotel_id,))
    conn.commit()

    if cursor.rowcount > 0:
        logger.info(f"Hotel {hotel_id} successfully cancelled.")
        conn.close()
        return f"Hotel {hotel_id} successfully cancelled."
    else:
        logger.warning(f"No hotel found with ID {hotel_id}.")
        conn.close()
        return f"No hotel found with ID {hotel_id}."
