import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Function to download XML file from URL
def download_xml_file(url, destination):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(destination, 'wb') as f:
                f.write(response.content)
            print("XML file downloaded successfully.")
        else:
            print(f"Failed to download XML file. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading XML file: {e}")

# Function to read conversion rate from XML file
def read_conversion_rate(xml_file, target_currency):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for cube in root.iter('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube'):
            if cube.attrib.get('currency') == target_currency:
                return float(cube.attrib.get('rate'))
        print(f"Conversion rate for {target_currency} not found in XML.")
        return None
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return None
    
# Function to create message based on conversion rate
def create_message(conversion_rate):
    today = datetime.today().strftime('%d/%m/%y')
    if conversion_rate is not None:
        # Comparing fetched rate to 9
        if conversion_rate > 9:
            # Write todays rate message
            message = f"{today} on kurss üle 8.00€"
            return message
        else:
            return None
    else:
        return f"Conversion rate for NOK not found for {today}."
    

def write_to_txt(message):
    try:
        if message:
            today = datetime.today().strftime('%d/%m/%y')
            file_path = 'C:\\kurss\\kurss.txt'
            # Check if the directory exists, create it if it doesn't
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            # Check if the file exists, create it if it doesn't
            if not os.path.exists(file_path):
                open(file_path, 'w').close()
            with open(file_path, 'a+') as txt_file:
                txt_file.seek(0)
                lines = txt_file.readlines()
                # Find the latest recorded date in the file
                latest_date = None
                for line in lines:
                    if 'on kurss üle' in line:
                        date_str = line.split(' ')[0]
                        date_datetime = datetime.strptime(date_str, '%d/%m/%y')
                        if latest_date is None or date_datetime > latest_date:
                            latest_date = date_datetime
                # Print latest date in file
                print("Latest date in file:", latest_date)
                # Compare current date with the latest recorded date
                today_datetime = datetime.strptime(today, '%d/%m/%y')
                print("Today's date:", today_datetime)
                # Write the message if it's a new day
                if latest_date is None or today_datetime > latest_date:
                    txt_file.write(message + '\n')
                    print("Message written to kurss.txt successfully.")
                else:
                    print("Message for today already exists in kurss.txt or it's older than the latest recorded date. New message was not added.")
       # Write log if rate isnt bigger than 9             
        else:
            print("No message to write.")
    except Exception as e:
        print(f"Error writing to text file: {e}")


if __name__ == "__main__":
    xml_file_url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?ae6860f7ed7aa6e4b4b4ec32efe84990"
    xml_file_destination = "eurofxref-daily.xml"
    download_xml_file(xml_file_url, xml_file_destination)
    
    target_currency = "NOK" 
    conversion_rate = read_conversion_rate(xml_file_destination, target_currency)
    message = create_message(conversion_rate)
    write_to_txt(message)
