import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture(scope="function")
async def browser_setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        base_url = "https://automationexercise.com/"
        await page.goto(base_url)
        await page.wait_for_load_state("domcontentloaded")
        yield page, base_url
        await context.close()

