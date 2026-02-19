import random

def flight_finder(destination: str, date: str) -> str:
    """Found flights to a destination on a specific date.

    Args:
        destination: The destination city.
        date: The date of travel.

    Returns:
        A list of available flights with prices.
    """
    # Mock data
    airlines = ["SkyHigh", "OceanAir", "BudgetFly"]
    flights = []
    for _ in range(3):
        airline = random.choice(airlines)
        price = random.randint(300, 800)
        time = f"{random.randint(0, 23)}:{random.randint(0, 59):02d}"
        flights.append(f"{airline} - ${price} - {time}")
    
    return "\n".join(flights)

def extract_pdf_budget(filepath: str) -> str:
    """Extracts budget information from a policy PDF.

    Args:
        filepath: path to the PDF file.
    
    Returns:
        The text content of the PDF.
    """
    # Mock implementation
    return "The maximum allowed budget for this trip is $2500 USD."

def currency_converter(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts a currency amount from one currency to another.

    Args:
        amount: The amount to convert.
        from_currency: The source currency code (e.g. USD, EUR, JPY, INR).
        to_currency: The target currency code (e.g. USD, EUR, JPY, INR).

    Returns:
        A string with the converted amount and currency.
    """
    # Mock rates
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "JPY": 150.0,
        "INR": 83.0
    }

    if from_currency not in rates or to_currency not in rates:
        return f"Unsupported currency. Supported: {', '.join(rates.keys())}"

    # Convert to USD first then to target
    amount_in_usd = amount / rates[from_currency]
    converted = int(amount_in_usd * rates[to_currency] * 100) / 100.0
    return f"{amount} {from_currency} = {converted} {to_currency}"

def hotel_finder(destination: str, check_in: str) -> str:
    """Finds hotels in a destination.

    Args:
        destination: The city to find hotels in.
        check_in: The check-in date.

    Returns:
        A list of available hotels.
    """
    hotels = ["Grand Plaza", "Cozy Inn", "City Center Hotel"]
    results = []
    for hotel in hotels:
        price = random.randint(100, 300)
        results.append(f"{hotel} - ${price}/night")
    return "\n".join(results)
