import os
import time

from fastapi import APIRouter, Request

from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from models.ResposeModels import ScrapingResponseModel

from utils import transform, aws_functions

router = APIRouter(prefix="/api/v1")

@router.get('/download_latest_data', response_model=ScrapingResponseModel)
def download_latest_data(request: Request) -> dict:

    download_folder = os.getenv('DOWNLOAD_FOLDER')
    filter_selection = os.getenv('FILTER_SELECTION')

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': download_folder, 'download.prompt_for_download': False, 'download.directory_upgrade': True}

    options.add_experimental_option('prefs', prefs)

    svc = webdriver.ChromeService(executable_path=binary_path)

    driver = webdriver.Chrome(options=options, service=svc)

    # Tempo mínimo de espera para as ações do navegador
    driver.implicitly_wait(10)

    url = os.getenv('URL_B3')

    driver.get(url)

    driver.find_element(by=By.ID, value='segment').send_keys(filter_selection)

    driver.find_element(by=By.LINK_TEXT, value='Download').click()

    # A instrução abaixo é necessária para garantir que o arquivo seja baixado
    time.sleep(5)

    driver.quit()

    file_names = os.listdir(download_folder)

    # Sort the file names by last modification time
    sorted_files = sorted(file_names, key=lambda f: os.path.getmtime(os.path.join(download_folder, f)), reverse=True)

    latest_filename = sorted_files[0]

    file_date = latest_filename.split('_')[1][0:8]

    options = {'encoding':'ISO-8859-1','skipfooter':2, 'sep':';', 'thousands':'.', 'decimal':',', 'header':1, 'index_col':False, 'engine': 'python'}

    file_path = f'{download_folder}/{latest_filename}'

    renamed_filename = latest_filename.replace(".csv",".parquet")

    renamed_file_path = f'{download_folder}/{renamed_filename}'

    request.app.app_logger.info(f'FilePath: {file_path} ::: RenamedFile: {renamed_file_path}')

    print(f'FilePath: {file_path} ::: RenamedFile: {renamed_file_path}')

    transform.csv_to_parquet(file_path, renamed_file_path, file_date, options)

    aws_functions.upload_to_s3(renamed_file_path,renamed_filename, '2mle', 'raw')

    if len(sorted_files) == 0:
        return {'message': 'No files found'}
    else:
        return {'message': 'Scraping Successful', 'filename' : latest_filename, 'file_date' : file_date}
    

