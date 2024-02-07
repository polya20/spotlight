"""Tests for basic interactions"""

import time
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .helpers import (
    get_tab,
    screenshot_exception,
    wait_for_tagged_element,
)


def test_tabs_available(
    webdriver: WebDriver,
    tallymarks_dataset: Any,
    frontend_base_url: str,
    skip_tour: None,
) -> None:
    """
    test to click tabs
    """

    from ._autogenerated_ui_elements import DataTestTags

    with screenshot_exception(webdriver):
        webdriver.get(frontend_base_url)
        driver = webdriver

        wait_for_tagged_element(webdriver, DataTestTags.HELP_BUTTON)

        time.sleep(1.0)

        wait_for_tagged_element(webdriver, DataTestTags.DATAGRID_ALL_TAB_BUTTON)
        num = int(
            wait_for_tagged_element(webdriver, DataTestTags.DATAGRID_ALL_COUNT).text
        )
        assert num > 10
        tab = wait_for_tagged_element(webdriver, DataTestTags.DATAGRID_ALL_TAB_BUTTON)
        tab.click()

        wait_for_tagged_element(webdriver, DataTestTags.DATAGRID_FILTERED_TAB_BUTTON)
        num = int(
            wait_for_tagged_element(
                webdriver, DataTestTags.DATAGRID_FILTERED_COUNT
            ).text
        )
        assert num > 10
        tab = wait_for_tagged_element(
            webdriver, DataTestTags.DATAGRID_FILTERED_TAB_BUTTON
        )
        tab.click()

        wait_for_tagged_element(webdriver, DataTestTags.DATAGRID_SELECTED_TAB_BUTTON)
        num = int(
            wait_for_tagged_element(
                webdriver, DataTestTags.DATAGRID_SELECTED_COUNT
            ).text
        )
        assert num == 0
        tab = wait_for_tagged_element(
            webdriver, DataTestTags.DATAGRID_SELECTED_TAB_BUTTON
        )

        tab.click()

        tab = get_tab(driver, "Scatter Plot")
        tab.click()

        tab = get_tab(driver, "Histogram")
        tab.click()

        tab = get_tab(driver, "Similarity Map")
        tab.click()

        tab = get_tab(driver, "Inspector")
        tab.click()


def test_tagged_elements_available(
    webdriver: WebDriver,
    tallymarks_dataset: Any,
    frontend_base_url: str,
    skip_tour: None,
) -> None:
    """
    test that elements with data-test-tag are available
    """
    from ._autogenerated_ui_elements import DataTestTags

    with screenshot_exception(webdriver):
        webdriver.get(frontend_base_url)

        driver = webdriver

        wait_for_tagged_element(webdriver, DataTestTags.HELP_BUTTON)

        for tag in [
            tag for name, tag in vars(DataTestTags).items() if not name.startswith("_")
        ]:
            if tag not in [
                DataTestTags.GLOBAL_LOADING_INDICATOR,
                DataTestTags.MESHVIEW_SETTINGS_DROPDOWN,
                DataTestTags.SEQUENCEVIEW_SETTINGS_DROPDOWN,
            ]:
                element = wait_for_tagged_element(webdriver, tag, 1)
                if "dropdown" in tag or "button" in tag:
                    element.click()
                driver.find_element(by=By.XPATH, value="//body").click()
