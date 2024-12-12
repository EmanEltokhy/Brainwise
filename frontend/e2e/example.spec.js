// const { chromium } = require("playwright");
const { test, expect } = require("@playwright/test");
const { request } = require("http");
// const assert = require("assert");

test.beforeEach("login", async ({ page }) => {
  // Perform login
  await page.goto("http://localhost:8080/");
  await page.getByPlaceholder("Enter National ID").click();
  await page.getByPlaceholder("Enter National ID").fill("101");
  await page.getByPlaceholder("Enter National ID").click();
  await page.getByPlaceholder("Enter your password").fill("123");
  await page.getByRole("button", { name: "Log In" }).click();
  await page.waitForURL("http://localhost:8080/dashboard");
  await page.reload();
});
// test("register", async ({ page }) => {
//   await page.goto("http://localhost:8080/");
//   await page.click('a:has-text("Register")');
//   await page.fill('input[placeholder="Enter First Name"]', "John");
//   await page.fill('input[placeholder="Enter Last Name"]', "Doe");
//   await page.fill('input[placeholder="Enter User Name"]', "johndoe");
//   await page.fill('input[placeholder="Enter Naiontal ID"]', "9876543210");
//   await page.fill('input[placeholder="Enter Phone Number"]', "1234567890");
//   await page.fill('input[placeholder="Enter your password"]', "password123");
//   await page.click('button:has-text("Register")');

//   // Wait for registration to complete
//   await page.waitForSelector(
//     'div.text-h4.text-center.text-teal.font-weight-bold.mb-5:has-text("Welcome to our cash website")'
//   );
// });

// test("dashboard-paymob", async ({ page, browser }) => {
//   await page.getByRole("button", { name: "Recharge" }).click();
//   await page.getByLabel("Enter Recharge amount").fill("40");
//   await page.getByRole("button", { name: "OK" }).click();
//   await page.waitForTimeout(2000);
//   await page.getByPlaceholder("Card Number").fill("5123456789012346");
//   await page.getByPlaceholder("Card Holder Name").fill("Test Account");
//   await page.getByPlaceholder("MM/YY").fill("12 / 25");
//   await page.getByPlaceholder("CVV").fill("123");
//   await page.pause();
//   await page.getByRole("button", { name: "PAY 40.00 EGP" }).click();
//   await page.waitForURL(url => {
//     const urlWithoutQueryParams = new URL(url).origin + new URL(url).pathname;
//     console.log(urlWithoutQueryParams);
//     return urlWithoutQueryParams === 'https://cf03-156-195-171-125.ngrok-free.app/account/api/callback';
//   });
//   await page.getByRole("button", { name: "Visit Site" }).click();
//   page.waitForSelector("div.v-card-title.error-dialog-title", {
//     visible: true,
//   });
//   page.locator("div").filter({ hasText: /^OK$/ }).click();

// });

// test("dashboard-amount", async ({ page }) => {
//   await page.waitForLoadState("networkidle");
//   await page.getByRole("button", { name: "01206997847" }).click();
//   await page
//     .locator("div")
//     .filter({ hasText: /^01206997847$/ })
//     .nth(1)
//     .click();
//   expect(page.locator("div.text-h3")).toHaveText(" EGP 1760.0");
//   await page.getByRole("button", { name: "01206997847" }).click();
//   await page
//     .locator("div")
//     .filter({ hasText: /^01100000000$/ })
//     .first()
//     .click();
//   expect(page.locator("div.text-h3")).toHaveText(" EGP 1196.5");
// });

test("dashboard-overview", async ({page})=>{
  await page.waitForLoadState('networkidle');
  const listItemsCount = await page.$$eval('.v-list-item', (items) => items.length);
  expect(listItemsCount).toBeGreaterThan(1);
});
test("recharge", async ({ page }) => {
  await page.getByRole("link", { name: "Services" }).click();
  await page.getByText("Mobile Recharge").click();
  await page.locator("div:nth-child(4) > .v-card").click();
  await page.getByRole("img").nth(4).click();
  await page.getByPlaceholder("Enter Mobile Number").fill("01552770782");
  await page.getByPlaceholder("Enter Recharge Amount").fill("20");
  await page.getByRole("button", { name: "Next" }).click();
  await page.waitForSelector("span#title:has-text('Payment Confirmation')")
  await page.getByRole("button", { name: "Next" }).click();
  await page.waitForSelector("span#title:has-text('Payment Successful')");

});
test("Donation", async ({ page }) => {
  await page.getByRole("link", { name: "Services" }).click();
  await  page.getByText("Donations").click();
  await page.locator("div:nth-child(4) > .v-card").click();
  await page.getByRole("img").nth(4).click();
  await page.getByPlaceholder("Enter Mobile Number").fill("01206997847");
  await page.getByPlaceholder("Enter Recharge Amount").fill("15");
  await page.getByRole("button", { name: "Next" }).click();
  await page.waitForSelector("span#title:has-text('Payment Confirmation')")
  await page.getByRole("button", { name: "Next" }).click();
  await page.waitForSelector("span#title:has-text('Payment Successful')");
});
test("transfer", async ({page})=>{
  await page.getByRole('link', { name: 'Services' }).click();
  await  page.getByText("Transfer").click();
  await page.getByPlaceholder('Enter Mobile Number').fill('01100000001');
  await page.getByPlaceholder('Enter Recharge Amount').fill('10');
  await page.getByRole('button', { name: 'Next' }).click();
  await page.waitForSelector("span#title:has-text('Payment Confirmation')")
  await page.getByRole('button', { name: 'Next' }).click();
  await page.waitForSelector("span#title:has-text('Payment Successful')");
});
test("utilities", async ({ page }) => {
  await page.getByRole("link", { name: "Services" }).click();
  await page.getByText("Utilities").click();
  await page.getByRole("img").nth(0).click();
  await page.getByRole("button", { name: "Select Service Provider" }).click();
  await page.getByText("South of Cairo").click();
  await page.getByPlaceholder("Enter Payment Code").fill("123456");
  await page.getByRole("button", { name: "Next" }).click();
  // await page.pause();
  await page.waitForSelector("span#title:has-text('Payment Confirmation')")
  await page.getByRole("button", { name: "Next" }).click();
  await page.waitForSelector("span#title:has-text('Payment Successful')");
  await page.getByRole("link", { name: "Services" }).click();
  await page.getByText("Utilities").click();
  await page.getByRole("button", { name: "Select Service Provider" }).click();
  await page.getByText("South of Cairo").click();
  await page.getByPlaceholder("Enter Payment Code").fill("123456");
  await page.getByRole("button", { name: "Next" }).click();
  await page.waitForSelector(
    "div.v-window-item.v-window-item--active.v-window-item:has-text('No Bill Found')"
  );
});
test("history", async ({ page }) => {
  await page.getByRole('link', { name: 'My History' }).click();
  await page.reload();
  await page.waitForLoadState("networkidle");
  const listItemsCount = await page.$$eval('.v-list-item', (items) => items.length);
  expect(listItemsCount).toBeGreaterThan(1);
});
