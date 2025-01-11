import os
from pom.pages.register_user_elements import RegisterUser
from pom.pages.add_to_cart_elements import AddToCart
import pytest
import pytest_asyncio
from playwright.async_api import expect


@pytest.mark.asyncio
class TestRegister:

    @pytest_asyncio.fixture(scope="function", autouse=True)
    async def setup(self, browser_setup):
        self.page, self.base_url = browser_setup

    async def test_register(self):
        try:
            register_obj = RegisterUser(self.page)
            await register_obj.open_signup_page_method()
            await register_obj.signup_form_submit_method()
            await register_obj.enter_details_method()

            acc_created_msg = await expect(register_obj.accVerifyMsg).to_have_text("Account Created!")
            print(acc_created_msg)

            await register_obj.continue_method()
            await register_obj.delete_acc_method()

            acc_delete_msg = await expect(register_obj.deleteAccMsg).to_have_text("Account Deleted!")
            print(acc_delete_msg)

            await register_obj.continue_method()

        except Exception as e:
            # Create screenshot folder if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            ss_path = "screenshots/register_user_failure.png"
            await self.page.screenshot(path=ss_path)
            print(f"Screenshot taken on failure: {ss_path}")
            print(f"Error: {str(e)}")
            pytest.fail(f"Test failed: {str(e)}")

    async def test_cart(self):
        try:
            cart_obj = AddToCart(self.page)
            await cart_obj.login_method()

            print_user_name = await expect(cart_obj.userVerify).to_have_text("chirag2")
            print(print_user_name)

            await cart_obj.add_to_cart_method()

            await expect(cart_obj.verifyItemInCart).to_have_text("Blue Top")
            await expect(cart_obj.verifyPrice).to_have_text("Rs. 500")
            await expect(cart_obj.verifyQty).to_have_text("1")
            await expect(cart_obj.verifyTotalPrice).to_have_text("Rs. 500")

            await cart_obj.remove_from_cart_method()
            await expect(cart_obj.verifyEmptyCart).to_have_text("Cart is empty!")

            await cart_obj.checkout_method()

            await cart_obj.cart_payment_method()

        except Exception as e:
            # Create screenshot folder if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            ss_path = "screenshots/add_to_cart_failure.png"
            await self.page.screenshot(path=ss_path)
            print(f"Screenshot taken on failure: {ss_path}")
            print(f"Error: {str(e)}")
            pytest.fail(f"Test failed: {str(e)}")
