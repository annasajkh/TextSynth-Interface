from pyppeteer import launch
import asyncio


async def get_elemets(page):
	await page.waitForSelector("#input_text")

	input_text = await page.querySelector("#input_text")

	submit_button = await page.querySelector("#submit_button")

	return input_text, submit_button

async def setup_browser():
    browser = await launch({"args":["--no-sandbox","--disable-setuid-sandbox"]})
    page = await browser.newPage()

    await page.goto("https://bellard.org/textsynth/")

    input_text, submit_button = await get_elemets(page)

    return browser, page, input_text, submit_button


async def main():
	while True:
	    browser, page, input_text, submit_button = await setup_browser()

	    await input_text.type(input(">") + " ")
	    await submit_button.click()

	    gtext = await page.querySelector("#gtext")
	    await asyncio.sleep(5)
	    result = await page.evaluate("(element) => element.innerText",gtext)

	    print(result)

	    await browser.close()


	
	



asyncio.get_event_loop().run_until_complete(main())


