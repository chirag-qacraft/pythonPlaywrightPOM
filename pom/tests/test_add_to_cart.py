import pytest
from playwright.async_api import expect,async_playwright
from pom.pages.add_to_cart_elements import AddToCart


@pytest.mark.asyncio
async def test_cart():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch browser
        context = await browser.new_context()  # Create a new context (similar to a browser profile)
        page = await context.new_page()

        cart_obj = AddToCart(page)

        await cart_obj.open_browser_method()
        await cart_obj.login_method()

        printusername = await expect(cart_obj.userVerify).to_have_text("chirag2")
        print(printusername)
        await page.wait_for_timeout(15000)

        await cart_obj.add_to_cart_method()

        await expect(cart_obj.verifyItemInCart).to_have_text("Blue Top")
        await expect(cart_obj.verifyPrice).to_have_text("Rs. 500")
        await expect(cart_obj.verifyQty).to_have_text("1")
        await expect(cart_obj.verifyTotalPrice).to_have_text("Rs. 500")

        await cart_obj.remove_from_cart_method()
        await expect(cart_obj.verifyEmptyCart).to_have_text("Cart is empty!")

        await cart_obj.checkout_method()

        await cart_obj.cart_payment_method()



