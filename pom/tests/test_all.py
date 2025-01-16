import os
from pom.pages.register_user_elements import RegisterUser
from pom.pages.add_to_cart_elements import AddToCart
import pytest, allure
import pytest_asyncio
from playwright.async_api import expect


@pytest.mark.asyncio
class TestAll:

    @pytest_asyncio.fixture(scope="function", autouse=True)
    async def setup(self, browser_setup):
        self.page, self.base_url = browser_setup

    @allure.feature("User Registration")
    @allure.story("Register a new user and delete the account")
    async def test_register(self):
        try:
            register_obj = RegisterUser(self.page)

            with allure.step("Open Signup page"):
                await register_obj.open_signup_page_method()

            with allure.step("Submit Signup page"):
                await register_obj.signup_form_submit_method()

            with allure.step("Enter User details"):
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

    @allure.feature("Cart Operations")
    @allure.story("Add and remove items from the cart, checkout and make payment")
    async def test_cart(self):
        try:
            cart_obj = AddToCart(self.page)
            await cart_obj.login_method()

            with allure.step("Verify user name after login"):
                print_user_name = await expect(cart_obj.userVerify).to_have_text("chirag2")
                allure.attach(str(print_user_name), name="User Name", attachment_type=allure.attachment_type.TEXT)
                print(print_user_name)

            with allure.step("Add item to the cart"):
                await cart_obj.add_to_cart_method()

            with allure.step("Verify item, price, quantity, and total in the cart"):
                await expect(cart_obj.verifyItemInCart).to_have_text("Blue Top")
                await expect(cart_obj.verifyPrice).to_have_text("Rs. 500")
                await expect(cart_obj.verifyQty).to_have_text("1")
                await expect(cart_obj.verifyTotalPrice).to_have_text("Rs. 500")

            with allure.step("Remove item from the cart"):
                await cart_obj.remove_from_cart_method()
                await expect(cart_obj.verifyEmptyCart).to_have_text("Cart is empty!")

            with allure.step("Proceed to checkout"):
                await cart_obj.checkout_method()

            with allure.step("Proceed to payment"):
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
