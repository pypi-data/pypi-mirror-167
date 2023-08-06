from ..chrome.webdriver import WebDriver as Chrome  # noqa
from ..firefox.webdriver import WebDriver as Firefox  # noqa
from ..edge.webdriver import WebDriver as Edge  # noqa
from ..safari.webdriver import WebDriver as Safari  # noqa
from .DownloadChromeDriver import *
from .DownloadGeckoDriver import *
from .DownloadEdgeDriver import *
from selenium_pro.webdriver.support.global_vars import set_global_driver
from selenium_pro.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess
import requests
import json
import platform
import urllib.request
from pathlib import Path
import plistlib
try:
    from winreg import *
except:
    pass
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
def get_mac_default_browser():
    browser=""
    try:
        PREFERENCES = (
        Path.home(),"Library","Preferences","com.apple.LaunchServices/com.apple.launchservices.secure.plist")
        NAMES = {
            "com.apple.safari": "Safari",
            "com.google.chrome": "Chrome",
            "org.mozilla.firefox": "Firefox",
        }
        with PREFERENCES.open("rb") as fp:
            data = plistlib.load(fp)
        for handler in data["LSHandlers"]:
            if handler.get("LSHandlerURLScheme") == "http":
                role = handler["LSHandlerRoleAll"]
                browser = NAMES[role]
                return browser
    except:
        pass
    return "Safari"
def get_default_browser(platform):
    browser=""
    if(platform=="win"):
        with OpenKey(HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
            browser = QueryValueEx(key, 'Progid')[0]
        if("chrome" in browser.lower()):
            browser="Chrome"
        elif("firefox" in browser.lower()):
            browser="Firefox"
        elif("msedge" in browser.lower()):
            browser="Edge"
        elif("safari" in browser.lower()):
            browser="Safari"
    elif(platform=="linux"):
        try:
            chrome_ver=get_chrome_version(platform, "")
        except:
            chrome_ver=""
        if(chrome_ver!=""):
            browser="Chrome"
        else:
            browser="Firefox"
    elif(platform=="mac"):
        browser=get_mac_default_browser()
    return browser
def start_driver(browser=None,port=0,options=None, service_args=None,desired_capabilities=None, service_log_path="driver.log",chrome_options=None, keep_alive=True,
    firefox_profile=None, firefox_binary=None,timeout=30, capabilities=None, proxy=None,firefox_options=None,log_path=None,verbose=None,
    reuse_service=False,quiet=False):
    global global_driver
    platform, architecture=get_platform_architecture()
    if(browser==None):
        browser=get_default_browser(platform)
        if(browser==""):
            browser="Chrome"
    file_extension=""
    if(platform=="win"):
        file_extension=".exe"
    if(desired_capabilities==None and browser=="Safari"):
        desired_capabilities=DesiredCapabilities.SAFARI
    if(browser=="Chrome"):
        try:
            driver=Chrome(executable_path="chromedriver"+file_extension, port=port,
                 options=options, service_args=service_args,
                 desired_capabilities=desired_capabilities, service_log_path=service_log_path,
                 chrome_options=chrome_options, keep_alive=keep_alive)
        except Exception as e:
            if("executable needs to be in PATH" in str(e) or "ChromeDriver only supports Chrome" in str(e)):
                download_chromedriver()
                driver=Chrome(executable_path="chromedriver"+file_extension, port=port,
                 options=options, service_args=service_args,
                 desired_capabilities=desired_capabilities, service_log_path=service_log_path,
                 chrome_options=chrome_options, keep_alive=keep_alive)
            else:
                raise RuntimeError(str(e))
    elif(browser=="Firefox"):
        try:
            driver=Firefox(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                 timeout=timeout, capabilities=capabilities, proxy=proxy,
                 executable_path="geckodriver"+file_extension, options=options,
                 service_log_path=service_log_path, firefox_options=firefox_options,
                 service_args=service_args, desired_capabilities=desired_capabilities, log_path=log_path,
                 keep_alive=keep_alive)
        except Exception as e:
            if("executable needs to be in PATH" in str(e)):
                download_geckodriver()
                driver=Firefox(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                 timeout=timeout, capabilities=capabilities, proxy=proxy,
                 executable_path="geckodriver"+file_extension, options=options,
                 service_log_path=service_log_path, firefox_options=firefox_options,
                 service_args=service_args, desired_capabilities=desired_capabilities, log_path=log_path,
                 keep_alive=keep_alive)
            else:
                raise RuntimeError(str(e))
    elif(browser=="Edge"):
        try:
            driver=Edge(executable_path='msedgedriver'+file_extension,
                 capabilities=capabilities, port=port, verbose=verbose, service_log_path=service_log_path,
                 log_path=log_path, keep_alive=keep_alive)
        except Exception as e:
            if("executable needs to be in PATH" in str(e)):
                download_safaridriver()
                driver=Edge(executable_path='msedgedriver'+file_extension,
                 capabilities=capabilities, port=port, verbose=verbose, service_log_path=service_log_path,
                 log_path=log_path, keep_alive=keep_alive)
            else:
                raise RuntimeError(str(e))
    elif(browser=="Safari"):
        try:
            driver=Safari(port=port, executable_path="/usr/bin/safaridriver"+file_extension, reuse_service=reuse_service,
                 desired_capabilities=desired_capabilities, quiet=quiet,
                 keep_alive=keep_alive, service_args=service_args)
        except Exception as e:
            raise RuntimeError(str(e))
    else:
        raise RuntimeError("This function only supports Firefox, Chrome, Edge and Safari")
    set_global_driver(driver)
    return driver