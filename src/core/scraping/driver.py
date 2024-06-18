from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Driver(Chrome):

    def __init__(
        self,
        options: Options = Options(),
        headless: bool = False,
        logs: bool = True,
        switches: bool = True,
        disable_images: bool = False,
        disable_js: bool = False,
        profile_path: str = "",
        download_location: str = "",
    ):
        prefs = {}
        if headless:
            options.add_argument("--headless")
        if logs == False:
            options.add_argument("--log-level=3")
        if switches == False:
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if disable_images:
            prefs["profile.managed_default_content_settings.images"] = 2
        if disable_js:
            prefs["profile.managed_default_content_settings.javascript"] = 2
        if profile_path:
            options.add_argument(f"user-data-dir={profile_path}")
        if download_location:
            options.add_argument(f"download.default_directory={download_location}")
        if prefs:
            options.add_experimental_option("prefs", prefs)
        super().__init__(options=options)
