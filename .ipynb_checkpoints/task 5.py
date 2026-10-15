import matplotlib.pyplot as plt
import pandas as pd
import requests

# Prepare the data retrieving connection
CLIENT_ID = "18184a8d-8fdc-46f3-86fc-ec35fae13b99"
endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN17850',
    'elements': 'mean(air_temperature P1D)',
    'referencetime': '2025-01-01/2025-12-31',
}

response = requests.get(endpoint, parameters, auth=(CLIENT_ID, ""))
json_data = response.json()

# Transforms JSON data to a local-callable list
records = []
if response.status_code == 200:
    for item in json_data["data"]:
        records.append(
            {
                "referenceTime": item["referenceTime"],
                "value": item["observations"][0]["value"],
            }
        )

# Transform the list to a dataframe
df = pd.DataFrame(records)
print(df.columns)
df["referenceTime"] = pd.to_datetime(df["referenceTime"])
df.set_index("referenceTime", inplace=True)

# Plot
plt.figure(figsize=(10, 4), dpi=100)
plt.plot(df.index, df["value"], color="#1f77b4", linewidth=1.5)
plt.title(
    "Daily Mean Air Temperature (SN17850 - 2025)", fontsize=12, fontweight="bold"
)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature (°C)", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Summary Statistics Table
summary_df = pd.DataFrame(
    {
        "Metric": ["Mean", "Median", "Min", "Max"],
        "Temperature (°C)": [
            df["value"].mean(),
            df["value"].median(),
            df["value"].min(),
            df["value"].max(),
        ],
    }
).round(2)

print("\n--- Temperature Summary Statistics (2025) ---")
print(summary_df.to_string(index=False))

def plot_moving_average(df):
    df = df.copy()

    # Calculate the 7-day moving average
    df["moving_average"] = df["value"].rolling(
        window=7, min_periods=1
    ).mean()

    plt.figure(figsize=(14, 6))

    # Plot daily temperatures using the datetime index
    plt.scatter(
        df.index,
        df["value"],
        s=15,
        alpha=0.6,
        label="Daily mean temperature",
    )

    # Plot the moving average
    plt.plot(
        df.index,
        df["moving_average"],
        color="red",
        linewidth=2,
        label="7-day moving average",
    )

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Mean Temperature in Ås (2025)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig("temperature_moving_average.png", dpi=150)
    plt.show()
    plt.close()


# Call the function outside its definition
plot_moving_average(df)