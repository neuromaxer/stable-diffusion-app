import requests

API_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "masterpiece wallpaper of modern car, shinny metal, city, low angle, intrincate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha, 8k masterpiece wallpaper of modern car, shinny metal, city, low angle, intrincate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha, 8k",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()