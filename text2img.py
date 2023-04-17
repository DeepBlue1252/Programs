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
    openai.organization = "org-uqp71zJlH9G3BhGunVAStNc0"
    openai.api_key = "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"
    url = imageURL(text)
    print(url)