from playwright.async_api import Page


class RegisterUser:
    def __init__(self, page: Page):
        self.page = page
        self.signUpLink = page.locator("//a[contains(text(),'Signup')]")

        #sign up page
        self.nameTextBox = page.locator("//input[@placeholder='Name']")
        self.emailTextBox = page.locator("(//input[@placeholder='Email Address'])[2]")
        self.signUpButton = page.locator("//button[text()='Signup']")

        #Registration page
        self.titleRadioButton = page.locator("//input[@id='id_gender1']")
        self.passwordTextBox = page.locator("//input[@id='password']")
        self.selectDayDD = page.locator("//select[@id='days']")
        self.selectMonthDD = page.locator("//select[@id='months']")
        self.selectYearDD = page.locator("//select[@id='years']")
        self.checkBox1 = page.locator("//input[@id='newsletter']")
        self.checkBox2 = page.locator("//input[@id='optin']")
        self.fNameTextBox = page.locator("//input[@id='first_name']")
        self.lNameTextBox = page.locator("//input[@id='last_name']")
        self.addrTextArea = page.locator("//input[@id='address1']")
        self.countryDD = page.locator("//select[@id='country']")
        self.stateTextBox = page.locator("//input[@id='state']")
        self.cityTextBox = page.locator("//input[@id='city']")
        self.zipcodeTextBox = page.locator("//input[@id='zipcode']")
        self.mobileTextBox = page.locator("//input[@id='mobile_number']")
        self.submitButton = page.locator("//button[text()='Create Account']")

        #Account Verification page
        self.accVerifyMsg = page.locator("//b[contains(text(),'Created')]")

        #Continue
        self.continueButton = page.locator("//a[text()='Continue']")

        #Delete Account link
        self.deleteAccLink = page.locator("//a[contains(text(),'Delete')]")
        self.deleteAccMsg = page.locator("//b[contains(text(),'Delete')]")


    async def open_signup_page_method(self):

        try:
            await self.signUpLink.click()
            print("Signup page open successfully")

        except Exception as e:
            print(f"Error: {e}")

    async def signup_form_submit_method(self):
            await self.nameTextBox.fill("Brett Lee")
            await self.emailTextBox.fill("brettlee58@gmail.com")

            await self.signUpButton.click()
            print("Sign Up successfully")

    async def enter_details_method(self):
            await self.titleRadioButton.click()
            await self.passwordTextBox.fill("tinu2")
            await self.selectDayDD.select_option(value="30")
            await self.selectMonthDD.select_option(label="January")
            await self.selectYearDD.select_option(label="1995")
            await self.checkBox1.click()
            await self.checkBox2.click()
            await self.fNameTextBox.fill("Robin")
            await self.lNameTextBox.fill("Singh")
            await self.addrTextArea.fill("iwefiejfeiwlfjo")
            await self.countryDD.select_option(value="India")
            await self.stateTextBox.fill("guj")
            await self.cityTextBox.fill("BRD")
            await self.zipcodeTextBox.fill("123456")
            await self.mobileTextBox.fill("1234567890")
            await self.submitButton.click()

    async def continue_method(self):
            await self.page.wait_for_timeout(15000)
            await self.continueButton.click()

    async def delete_acc_method(self):
            await self.deleteAccLink.click()







