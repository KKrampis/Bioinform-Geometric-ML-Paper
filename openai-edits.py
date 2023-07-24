import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Edit.create(
  model="text-davinci-edit-001",
  input="While the hidden layers can have an arbitrary number of neurons each, based on the complexity of the label classification problem we need the ANN to resolve , the input layer has the numbers of neurons require to receive the composite data",
  instruction="a research manuscript reference in bibtext format from the deep learning literatute for this text ",
  n=5
)

response = openai.Image.create(
  prompt="create a graphic demonstrating how a matrix multiplication and transformation rotates a geometric object on 2D plane",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

https://oaidalleapiprodscus.blob.core.windows.net/private/org-ZlV6lQ6nskPqH4KarhK2BAU0/user-wXgMHlV8nxIwnLXKTO2cvtCk/img-4sbIA5WZAkVr3da0OXcJHhlp.png?st=2023-04-17T16%3A41%3A59Z&se=2023-04-17T18%3A41%3A59Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-17T17%3A25%3A59Z&ske=2023-04-18T17%3A25%3A59Z&sks=b&skv=2021-08-06&sig=gRHu8ezb0DrKmlf0zOu0iGKiAMtYF7ZQyvKmUkoqKXU%3D

https://oaidalleapiprodscus.blob.core.windows.net/private/org-ZlV6lQ6nskPqH4KarhK2BAU0/user-wXgMHlV8nxIwnLXKTO2cvtCk/img-t3rq0YpoZKxBOUuDL6hbfN2E.png?st=2023-04-20T06%3A01%3A31Z&se=2023-04-20T08%3A01%3A31Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-20T05%3A24%3A19Z&ske=2023-04-21T05%3A24%3A19Z&sks=b&skv=2021-08-06&sig=pWK0mFEJ1d/aqa0mGFiIGfAUMOuYe1osTtAJVZvSp0s%3D
