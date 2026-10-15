import pandas as pd
import requests
import yaml

CLIENT_ID = "60df8b0f-fba3-496d-968a-50f82792f8f5"
ENDPOINT = "https://frost.met.no/observations/v0.jsonld?sources=SN17850&referencetime=2025-01-01%2F2025-12-31&elements=max(air_temperature%20P1D)"


def find_heatwaves(temperatures, threshold=27, min_days=5):
    """Return the start and end dates of all heatwaves."""
    temperatures = temperatures.sort_index()

    heatwaves = []
    start_date = None
    previous_date = None
    consecutive_days = 0

    for date, temp in temperatures.items():
        # A missing observation or a date gap breaks the sequence
        consecutive_date = (
            previous_date is not None
            and (date.normalize() - previous_date.normalize()).days == 1
        )

        if not consecutive_date:
            if consecutive_days >= min_days:
                heatwaves.append(
                    f"{start_date:%Y-%m-%d} - "
                    f"{previous_date:%Y-%m-%d}"
                )
            consecutive_days = 0
            start_date = None

        if pd.notna(temp) and temp >= threshold:
            if consecutive_days == 0:
                start_date = date

            consecutive_days += 1
        else:
            if consecutive_days >= min_days:
                heatwaves.append(
                    f"{start_date:%Y-%m-%d} - {date:%Y-%m-%d}"
                )
                # The end date should be the previous hot day
                heatwaves[-1] = (
                    f"{start_date:%Y-%m-%d} - "
                    f"{previous_date:%Y-%m-%d}"
                )

            consecutive_days = 0
            start_date = None

        previous_date = date

    # Include a heatwave that reaches the final observation
    if consecutive_days >= min_days:
        heatwaves.append(
            f"{start_date:%Y-%m-%d} - {previous_date:%Y-%m-%d}"
        )

    return heatwaves


def count_heatwaves(station_id, year, station_name=None, threshold=27, min_days=5):
    """Fetch station observations, count heatwaves and write YAML."""

    parameters = {
        "sources": station_id,
        "elements": "max(air_temperature P1D)",
        "referencetime": f"{year}-01-01/{year}-12-31",
        "timeoffsets": "default",
        "levels": "default",
    }

    response = requests.get(
        ENDPOINT,
        params=parameters,
        auth=(CLIENT_ID, ""),
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()

    records = []

    for item in data.get("data", []):
        observations = item.get("observations", [])

        if observations:
            records.append({
                "referenceTime": item["referenceTime"],
                "value": observations[0]["value"],
            })

    if not records:
        raise ValueError(
            f"No temperature observations found for "
            f"{station_id} in {year}."
        )

    df = pd.DataFrame(records)
    df["referenceTime"] = pd.to_datetime(df["referenceTime"])
    df = df.drop_duplicates("referenceTime")
    df = df.set_index("referenceTime").sort_index()

    # Find heatwave date ranges
    dates = find_heatwaves(
        df["value"],
        threshold=threshold,
        min_days=min_days,
    )

    if station_name is None:
        station_name = station_id

        
    summary = {
        "dates": dates,
        "station_id": station_id,
        "station_name": station_name,
        "year": year,
    }

    filename = "heatwave_summary_.yaml"

    with open(filename, "w", encoding="utf-8") as file:
        yaml.safe_dump(
            summary,
            file,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )

    print(f"Number of heatwaves: {len(dates)}")
    print(f"Summary saved to {filename}")

    return summary


# Run the task for Ås in 2025
summary = count_heatwaves("SN17850", 2025, station_name="Ås")