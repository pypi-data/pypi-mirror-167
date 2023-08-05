from ..chrome.webdriver import WebDriver as Chrome  # noqa
from selenium_pro.webdriver.support.global_vars import set_global_driver
import subprocess
import requests
import json
import platform
import urllib.request
def get_chrome_version():
    process = subprocess.Popen(
        ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
    )
    version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
    version=version.split(".")[0]
    return version
def download_driver(file_extension):
    version=get_chrome_version()
    url=json.loads(requests.get("https://xpsiq1mh93.execute-api.us-east-2.amazonaws.com/default/getdriverlinks",verify=False).text)[version]["url"]
    print("Downloading chromedriver...")
    urllib.request.urlretrieve(url, 'chromedriver'+file_extension)
def start_driver():
    global global_driver
    browser="Chrome"
    ostype=platform.system()
    if("Windows" in ostype):
        file_extension=".exe"
    if(browser=="Chrome" and "Windows" in ostype):
        try:
            driver=Chrome("chromedriver"+file_extension)
        except Exception as e:
            if("executable needs to be in PATH" in str(e) or "ChromeDriver only supports Chrome" in str(e)):
                download_driver(file_extension)
                driver=Chrome("chromedriver"+file_extension)
            else:
                print("EXCEPTION:-",e)
    else:
        print("This function only supports Windows")
        return None
    set_global_driver(driver)
    return driver
