import pandas as pd
import logging
import gspread
from google.oauth2.service_account import Credentials
from SE_pro_scrape import webscraper
logging.basicConfig(filename="SEpro.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def make_csv():
    try:
        names, prices,volumes = webscraper()

        my_dict = {"Name" : names , "Price" : prices , "Volume" : volumes}
        thecsv = pd.DataFrame(my_dict)
        thecsv.to_csv("Crypto.csv", index=False)
        thecsv.to_csv(r"C:\Users\Hadid haider channa\dist\Crypto.csv", index=False)
        logging.info(f"File created")
        print("File created")
        
    except Exception as e:
        logging.error(f"Exception in making csv : {e}")
        print(f"Exception in making csv : {e}")
    except TypeError or NameError as e:
        logging.error(f"Error in making csv: {e}")
        print(f"Error in making csv: {e}")

def sheet_data():
    try:
        make_csv()
        path=r"C:\Users\Hadid haider channa\credentials.json"
        scope =["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(path,scopes=scope)
        client=gspread.authorize(creds)
        sheet_id = "1HKi2J0aCFsSy1IS9MUd4Per_BaboHtj4lK5dDVK1eVo"
        
        sheet=client.open_by_key(sheet_id)
        worksheet= sheet.get_worksheet(0)
        df=pd.read_csv("Crypto.csv")
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        worksheet.format("A1:Z1",{"textFormat" : {"bold" : True}})
        logging.info("Sheet updated succefully")
        print("Sheet updated")
    except Exception as e :
        logging.error(f"Exception in updating sheets : {e}")
        print(f"Exception in updating sheets : {e}")
    except TypeError or NameError as e :
        logging.error(f"Error in updating sheets : {e}")
        print(f"Error in updating sheets {e}")


