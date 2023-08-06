import click, requests, json, os
import pandas as pd
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

# Allow the user to ingest data from a file
def ingest_data(path: str, customer: str) -> str:
    # Ensure file exists
    if not os.path.exists(path):
        raise Exception("File does not exist")

    # Accept csv files only
    if not path.endswith(".csv"):
        raise Exception("Invalid file format. Expected CSV")

    # Make connection to API and send data
    files={
        'file': [(os.path.basename(path)), open(path,'rb'), 'text/csv']
    }
    response = requests.request("POST", f"{BASE_URL}/api/v1/customers/{customer}/ingest", data={}, files=files)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json().get('data', None) or response.text

# Allow the user to retrieve raw timeseries data points from the database for onecustomer, set of timeseries and date range.
def save_timeseries_to_file(folder: str, customer: str, asset: str, timeseries: list, begin_date: datetime=None, end_date: datetime=None):
    # Build dates url parameters
    date_from = (begin_date and f"&date_from={begin_date.isoformat()}") or ""
    date_to = (end_date and f"&date_to={end_date.isoformat()}") or ""

    # Send request
    url = f"{BASE_URL}/api/v1/customers/{customer}/assets/{asset}?timeseries={','.join(timeseries)}{date_from}{date_to}"
    response = requests.request("GET", url, data={})

    if response.status_code != 200:
        raise Exception(response.text)

    res_data = response.json()

    if len(res_data) < 1:
        return "File not saved: No records found"
    
    # Convert to dataframe and save
    df = pd.DataFrame(res_data)

    # Build path
    filename = datetime.now().isoformat()+".csv"
    path = os.path.join(folder, filename)
    
    # Write csv
    df.to_csv(path)
    return "File saved to - "+os.path.abspath(path)

# Allow the user to compute statistics for a specific customer, timeseries and date range
def compute_stats(data: str) -> dict:
    response = requests.request("POST", f"{BASE_URL}/api/v1/stats/", data=data)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()

# CLI application
@click.command()
@click.option("--ingest", required=False, type=str, help="Ingest data from a csv file, with the filename as the asset name.")
@click.option("--datapoints_out", required=False, type=str, help="Retrieve raw timeseries data points and save to a specified directory")
@click.option("--stats", required=False, type=str, help="Compute stats based on the passed JSON configuration (use `--conf_example` to show example configuration)")
@click.option("--conf_example", is_flag=True, help="Compute stats based on the passed JSON configurationa")
def execute_cli(ingest, datapoints_out, stats, conf_example):
    if ingest:
        # Using prompts for now.
        # Will go through the click docs indepth later to know how args should be passed
        customer = input('Customer name: ')
        print(ingest_data(
            path=ingest,
            customer=customer
        ))
        # try:
        # except Exception as e:
        #     print("Error:", e)
    elif datapoints_out:
        # Using prompts for now.
        # Will go through the click docs indepth later to know how args should be passed
        customer = input('Customer name: ')
        asset = input('Asset: ')
        timeseries = input('Timeseries (separated by comma): ')
        begin_date = input('Begin (YYYY-MM-DD H:M:S): ')
        end_date = input('End (YYYY-MM-DD H:M:S): ')

        try:
            print(save_timeseries_to_file(
                folder=datapoints_out,
                customer=customer,
                asset=asset,
                timeseries=[x.strip() for x in timeseries.split(',')],
                begin_date=begin_date and datetime.strptime(begin_date, "%Y-%m-%d %H:%M:%S"),
                end_date=end_date and datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
            ))
        except Exception as e:
            print("Error:", e)
    elif stats:
        try:
            for customer, c_val in compute_stats(data=stats).items():
                print(f"\n{customer}:")
                for asset, a_val in c_val.items():
                    print(f"  {asset}:")
                    for ts, ts_val in a_val.items():
                        print(f"    {ts}:")
                        if ts_val:
                            for stat, stat_val in ts_val.items():
                                print(f"      [*] {stat} - {stat_val}")
                        else:
                            print(f"      [*] -")
        except Exception as e:
            print("Error:", e)
    elif conf_example:
        print(str("'"+json.dumps({ 
                "target": [
                    {
                        "customer": "CustomerWind", 
                        "asset": "turbine01", 
                        "timeseries": [
                            "generator___mechanical___speed", 
                            "generator___temperature"
                        ]
                    }, 
                    { 
                        "customer": "NewCustomer", 
                        "asset": "electric01", 
                        "timeseries": [
                            "inverter___eletrical___frequency", 
                            "generator___electrical___power_production"
                        ]
                    }
                ], 
                "stats": [ "avg", "min", "max", "std"],
                "begin_date": "2012-07-01T10:00:00", 
                "end_date": "2012-07-02T12:00:00" 
            })+"'").replace(" ", ""))

if __name__ == '__main__':
    execute_cli()
