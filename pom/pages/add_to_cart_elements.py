from playwright.async_api import Page

class AddToCart:
    def __init__(self, page:Page):
        self.page = page

        # Login page
        self.loginLink = page.locator("//a[contains(text(),'Signup')]")
        self.loginEmailTextBox = page.locator("//form[contains(@action,'login')]//child::input[@name='email']")
        self.passwordTextBox = page.locator("//input[@name='password']")
        self.loginButton = page.locator("//button[text()='Login']")

        # User verify
        self.userVerify = page.locator("//b[contains(text(),chirag)]")

        # Product Add To Cart
        self.productLink = page.locator("//a[contains(text(),'Products')]//parent::li")
        self.addToCart = page.locator("(//a[text()='Add to cart'])[1]")
        self.contShoppingButton = page.locator("//button[contains(text(),'Continue')]")
        self.cartLink = page.locator("//a[contains(text(),'Cart')]//parent::li")

        # Verify Product
        self.verifyItemInCart = page.locator("//a[contains(text(),'Blue')]")
        self.verifyPrice = page.locator("(//p[contains(text(),'500')])[1]")
        self.verifyQty = page.locator("//button[text()='1']")
        self.verifyTotalPrice = page.locator("//p[@class='cart_total_price']")

        #Remove From Cart
        self.removeItemFromCart = page.locator("//a[@class='cart_quantity_delete']")
        self.verifyEmptyCart = page.locator("//b[contains(text(),'empty!')]")


        #Checkout and Place Order
        self.checkoutButton = page.locator("//a[contains(text(),'Checkout')]")
        self.placeOrderButton = page.locator("//a[contains(text(),'Place')]")
        self.cardNameTextBox = page.locator("//input[@name='name_on_card']")
        self.cardNumberTextBox = page.locator("//input[@name='card_number']")
        self.cardCvcTextBox = page.locator("//input[@name='cvc']")
        self.cardExpiryMonthTextBox = page.locator("//input[@name='expiry_month']")
        self.cardExpiryYearTextBox = page.locator("//input[@name='expiry_year']")
        self.paymentButton = page.locator("//button[@id='submit']")

        #Invoice Download
        self.invoiceDownload = page.locator("//a[contains(text(),'Invoice')]")

    async def open_browser_method(self):

            await self.page.goto("https://automationexercise.com/")
            await self.loginLink.wait_for(state="visible")


    async def login_method(self):
        await self.loginLink.click()
        await self.loginEmailTextBox.fill("chirag2@gmail.com")
        await self.passwordTextBox.fill("chirag2")
        await self.loginButton.click()

    async def add_to_cart_method(self):
        await self.productLink.click()
        await self.addToCart.hover()
        await self.addToCart.click()
        await self.contShoppingButton.click()
        await self.cartLink.click()

    async def remove_from_cart_method(self):
        await self.removeItemFromCart.click()

    async def checkout_method(self):
        await self.productLink.click()
        await self.addToCart.hover()
        await self.addToCart.click()
        await self.contShoppingButton.click()
        await self.cartLink.click()
        await self.checkoutButton.click()
        await self.placeOrderButton.click()

    async def cart_payment_method(self):
        await self.cardNameTextBox.fill("robin")
        await self.cardNumberTextBox.fill("12345678")
        await self.cardCvcTextBox.fill("311")
        await self.cardExpiryMonthTextBox.fill("01")
        await self.cardExpiryYearTextBox.fill("2040")
        await self.paymentButton.click()
        await self.invoiceDownload.click()

        await self.page.wait_for_timeout(15000)
