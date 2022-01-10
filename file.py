import requests
import praw
import textwrap
from PIL import Image, ImageDraw, ImageFont
from lxml import html
from instabot import Bot

def titleToImage(theTitle,number):
    
    para = textwrap.wrap(theTitle, width=15)
    text_color = "rgb(255, 255, 255)"
    MAX_W, MAX_H = 460, 200
    im = Image.new('RGB', (480, 600), color = (0, 0, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Simple Chalk.ttf", size=45)

    current_h, pad = 50, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line,fill=text_color,font=font)
        current_h += h + pad

    im.save("title"+str(number)+".png")

def bodyToImage(theBody,number):
    
    para = textwrap.wrap(theBody, width=15)
    text_color = "rgb(255, 255, 255)"
    MAX_W, MAX_H = 460, 200
    im = Image.new('RGB', (480, 600), color = (0, 0, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Simple Chalk.ttf", size=45)

    current_h, pad = 50, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line,fill=text_color,font=font)
        current_h += h + pad

    im.save("body"+str(number)+".png")



SLIDE1 = [0]*26
SLIDE2 = [0]*26
reddit = praw.Reddit(client_id='FB_n-nF4R3VjEw', \
                     client_secret='nwEl66Nv1IARZ5HgDkCYtrT4fAY', \
                     user_agent='', \
                     username='', \
                     password='')

subreddit = reddit.subreddit('twosentencehorror')
i=0
hot_subreddit = subreddit.top("day",limit=3) 
for submission in hot_subreddit:
    print("\nPost #",i)
    SLIDE1[i] = submission.title
    SLIDE2[i] = submission.selftext
    print("Title",i,"added to index ",i," in SLIDE1.")
    print("Body",i,"added to index ",i," in SLIDE2.")
    titleToImage(submission.title,i)
    bodyToImage(submission.selftext,i)
    i+=1



bot = Bot()
bot.login(username = "",password="")
bot.upload_photo("images/title0.jpg",caption="title0 test")
bot.upload_photo("images/body0.jpg",caption="body0 test")
