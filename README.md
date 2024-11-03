# 2024-Duke-AI-Hackathon

# Inspiration:
Nutritional deficiency is one of America's greatest public health challenges.

According to the CDC, only 12.3 and 10.0 percent of Americans are meeting recommended intake values for fruits and vegetables, respectively. As Americans continue to consume more ultra-processed foods, communicating healthy nutritional guidelines only becomes more important. While people can get nutritional advice from professionals, those services can be unaffordable and inconvenient.

# What it does:
NutriSync contains two functionalities, which both aim to provide free and personalized nutritional information:

The Diet Balancer takes in a user’s biographical information and food consumption and determines if that person is meeting their daily nutritional requirements in 13 different metrics. It then provides a summary of their nutritional health, a complementary healthy recipe to balance their diet, and details on specific nutritional deficiencies and foods rich in those nutrients. 

The Diet Advisor answers questions associated with nutrition and health, keeping track of previous questions and responses to further enhance its responses. It can also provide responses in 6 differing tones. 

# How We Built It:
We built NutriSync using the OpenAI API, Streamlit, the Requests library, the Beautiful Soup 4 library, and Python. In Diet Balancer, the biographical information is first stored for later use and up to 10 foods currently part of the user’s diet are input, and stored in a list. Using both the biometric and food diet data, a prompt to be passed to an OpenAI API call is crafted by the program, asking the LLM to determine which nutrients were sufficiently and insufficiently represented in the user’s diet, which foods contribute to a good diet already, suggestions of foods to correct the user’s diet (if necessary), and a recipe that can use these supplemental foods as ingredients. The OpenAI API call response was a JSON file, which the program parses in order to display the suggested information. 

Furthermore, the Requests library was utilized to find a visual example of the first recommended food, or food contributing to a healthy diet, by web-scraping Google Images. 

As for Diet Advisor, a singular text field takes input from the user and passes that to an OpenAI call, outputting the response of the API call back to the user. Moreover, different tones of the response messages were created by altering the “content” field of the system. 


# Challenges we ran into:
This is our first hackathon working with AI, so we initially had some trouble with aspects such as Git and the OpenAI library. Additionally, it took us a significant amount of time to narrow down our ideas into something specific and executable. 

# Accomplishments that we're proud of:
Once again, this is our first hackathon, and we are proud of being able to implement OpenAI and StreamLit to create two intuitive and useful web apps in such a short period of time. Additionally, we were able to implement additional features such as web scraping to find images of recommended foods and customizing the tone of the chatbot. 

# What we learned
We learned how to work with tools such ChatGPT, StreamLit, and BeautifulSoup4. We also learned about how we could apply AI towards the field of Health and Wellness, and had the great experience of learning what a hackathon is like at Duke!

# What's next for NutriSync
Some ideas we have for improving NutriSync include making it more accessible to more people by providing translations to different languages and incorporating disability accessibility. Other ways we are looking into improving NutriSync include adding more micronutrients, taking into consideration the quantity of each food consumed, and providing specific values for the amounts of each nutrient consumed. 



