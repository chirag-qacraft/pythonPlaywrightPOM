import pytest
import asyncio
from playwright.async_api import expect,async_playwright
from pytest_playwright.pytest_playwright import browser

@pytest.mark.asyncio
async  def test_drag_drop_frame():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager", timeout=150000,
                        wait_until="networkidle")

        frm = page.frame_locator("(//iframe[@class='demo-frame lazyloaded'])[1]")

        await frm.locator("//h5[text()='High Tatras 2']").drag_to(frm.locator("//div[@id='trash']"))

        await page.wait_for_timeout(15000)
