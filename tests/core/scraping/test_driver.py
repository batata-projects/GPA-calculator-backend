from src.core.scraping.driver import Driver


class TestDriver:
    def test_driver(self) -> None:
        driver = Driver(
            headless=True,
            logs=False,
            switches=False,
            disable_images=True,
            disable_js=True,
        )
        driver.quit()
        assert True
