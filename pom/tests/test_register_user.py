import pytest
from playwright.async_api import expect, async_playwright
from pom.pages.register_user_elements import RegisterUser


@pytest.mark.asyncio
async def test_register():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch browser
        context = await browser.new_context()  # Create a new context (similar to a browser profile)
        page = await context.new_page()

        register_obj = RegisterUser(page)
        await register_obj.open_browser_method()
        await register_obj.open_signup_page_method()
        await register_obj.signup_form_submit_method()
        await register_obj.enter_details_method()

        accCreatedMsg = await expect(register_obj.accVerifyMsg).to_have_text("Account Created!")
        print(accCreatedMsg)

        await register_obj.continue_method()
        await register_obj.delete_acc_method()

        accDeletedMsg = await expect(register_obj.deleteAccMsg).to_have_text("Account Deleted!")
        print(accDeletedMsg)

        await register_obj.continue_method()


