"""
@Time ： 2024-10-27
@Auth ： Adam Lyu
"""
import sqlite3
from datetime import date, datetime
from typing import Optional, Union
from langchain_core.tools import tool
from scripts.populate_database import db
from utils.logger import logger


@tool
def search_car_rentals(
        location: Optional[str] = None,
        name: Optional[str] = None,
        price_tier: Optional[str] = None,
        start_date: Optional[Union[datetime, date]] = None,
        end_date: Optional[Union[datetime, date]] = None,
) -> list[dict]:
    """
    Search for car rentals based on location, name, price tier, start date, and end date.

    Returns:
        list[dict]: A list of car rental dictionaries matching the search criteria.
    """
    logger.info("Starting search_car_rentals with parameters.")
    logger.debug(f"Parameters: location={location}, name={name}, price_tier={price_tier}, "
                 f"start_date={start_date}, end_date={end_date}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = "SELECT * FROM car_rentals WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")

    logger.debug(f"Executing query: {query} with params: {params}")
    cursor.execute(query, params)
    results = cursor.fetchall()

    ret = [dict(zip([column[0] for column in cursor.description], row)) for row in results]
    conn.close()

    logger.info(f"search_car_rentals found {len(ret)} results.")
    return ret


@tool
def book_car_rental(rental_id: int) -> str:
    """
    Book a car rental by its ID.

    Returns:
        str: A message indicating whether the car rental was successfully booked or not.
    """
    logger.info(f"Attempting to book car rental with ID {rental_id}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("UPDATE car_rentals SET booked = 1 WHERE id = ?", (rental_id,))
    conn.commit()

    if cursor.rowcount > 0:
        logger.info(f"Car rental {rental_id} successfully booked.")
        conn.close()
        return f"Car rental {rental_id} successfully booked."
    else:
        logger.warning(f"No car rental found with ID {rental_id}.")
        conn.close()
        return f"No car rental found with ID {rental_id}."


@tool
def update_car_rental(
        rental_id: int,
        start_date: Optional[Union[datetime, date]] = None,
        end_date: Optional[Union[datetime, date]] = None,
) -> str:
    """
    Update a car rental's start and end dates by its ID.

    Returns:
        str: A message indicating whether the car rental was successfully updated or not.
    """
    logger.info(f"Updating car rental {rental_id} with new dates.")
    logger.debug(f"New dates: start_date={start_date}, end_date={end_date}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    if start_date:
        cursor.execute("UPDATE car_rentals SET start_date = ? WHERE id = ?", (start_date, rental_id))
    if end_date:
        cursor.execute("UPDATE car_rentals SET end_date = ? WHERE id = ?", (end_date, rental_id))

    conn.commit()

    if cursor.rowcount > 0:
        logger.info(f"Car rental {rental_id} successfully updated.")
        conn.close()
        return f"Car rental {rental_id} successfully updated."
    else:
        logger.warning(f"No car rental found with ID {rental_id}.")
        conn.close()
        return f"No car rental found with ID {rental_id}."


@tool
def cancel_car_rental(rental_id: int) -> str:
    """
    Cancel a car rental by its ID.

    Returns:
        str: A message indicating whether the car rental was successfully cancelled or not.
    """
    logger.info(f"Attempting to cancel car rental with ID {rental_id}")

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("UPDATE car_rentals SET booked = 0 WHERE id = ?", (rental_id,))
    conn.commit()

    if cursor.rowcount > 0:
        logger.info(f"Car rental {rental_id} successfully cancelled.")
        conn.close()
        return f"Car rental {rental_id} successfully cancelled."
    else:
        logger.warning(f"No car rental found with ID {rental_id}.")
        conn.close()
        return f"No car rental found with ID {rental_id}."
