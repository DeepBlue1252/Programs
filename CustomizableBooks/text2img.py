import os
import openai

def imageURL(text):
    response = openai.Image.create(
    prompt=text,
    n=1,
    size="512x512"
    )
    image_url = response['data'][0]['url']

def main():
    openai.organization = "key"
    openai.api_key = "key"
    url = imageURL(text)
    print(url)
