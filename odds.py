from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


def main():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    #client = discord.Client()

    client = commands.Bot(command_prefix='.')

    @client.event
    async def on_ready():
        print('Bot is ready!')

    @client.command()
    async def odds(ctx):
        odds = get_odds()
        await ctx.send(odds)
        print("Odds successful")

    client.run(TOKEN)


def get_odds():
    web = 'https://www.betfair.com/exchange/plus/en/politics-betting-2378961'
    path = 'C:/Users/louis/Downloads/chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(path)
    driver.minimize_window()
    driver.get(web)

    try:
        accept = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        accept.click()
    finally:
        print("Closed pop-up")
    odds = driver.find_element_by_xpath(
        '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[2]/div/div/div/table/tbody/tr[2]/td[4]/button/div/span[1]')
    print('Odds:', odds.text)
    odds_value = odds.text
    driver.quit()
    return odds_value


if __name__ == "__main__":
    print(main())
