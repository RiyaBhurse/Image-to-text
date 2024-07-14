import pathlib
import textwrap
import time
import google.generativeai as genai
genai.configure(api_key="AIzaSyBUtpL2m21nHa28G0Lic54AiuqtEOy_9AY")
# from IPython.display import display
import PIL.Image

img = PIL.Image.open('image.jpg')
model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content(img)
starttime = time.time()
# to_markdown(response.text)
response = model.generate_content(["tell me what all colours do you see in the pic", img])
endtime = time.time()
# to_markdown(response.text)
time_taken = endtime - starttime
print("Time taken: ", time_taken)
print(response.text)