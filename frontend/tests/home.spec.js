// const { chromium } = require("playwright");
const {test, expect } = require('@playwright/test')
// const assert = require("assert");

test('url',async ({page}) => {
  // const browser = await chromium.launch({
  //   slowMo: 500,
  //   headless: false, // Set to true for headless mode
  // });
  // const context = await browser.newContext();
  // const page = await context.newPage();

  // Open the webpage
  await page.goto("http://localhost:8080"); // Replace with the actual URL of your website

  // Perform login
  await page.fill('input[placeholder="Enter National ID"]', "101"); // Replace with a valid National ID
  await page.fill('input[placeholder="Enter your password"]', "123"); // Replace with a valid password
  await page.click('button:has-text("Log In")');
  await page.waitForURL();

  // Wait for login to complete
  // test(true == true);
  expect(page.url).toBe("http://localhost:8080/dashboard");

  // Perform registration
  // await page.click('a:has-text("Register")');
  // await page.fill('input[placeholder="Enter First Name"]', 'John');
  // await page.fill('input[placeholder="Enter Last Name"]', 'Doe');
  // await page.fill('input[placeholder="Enter User Name"]', 'johndoe');
  // await page.fill('input[placeholder="Enter National ID"]', '9876543210');
  // await page.fill('input[placeholder="Enter Phone Number"]', '1234567890');
  // await page.fill('input[placeholder="Enter your password"]', 'password123');
  // await page.click('button:has-text("Register")');

  // // Wait for registration to complete
  // await page.waitForSelector('div.text-h4.text-center.text-teal.font-weight-bold.mb-5:has-text("Welcome to our cash website")');

  // // Access key features
  // await page.waitForSelector('h2.mb-16.text-teal.font-weight-regular:has-text("Key Features")');
  // const cardTitles = await page.$$eval('v-card-title', (elements) => elements.map((el) => el.textContent));
  // console.log('Card Titles:', cardTitles);

  // Close the browser
  // await browser.close();
});
