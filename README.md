# NutriSync

### Built during the 2024 Duke AI Hackathon

## Inspiration
Nutritional deficiency is one of America's greatest public health challenges.

According to the CDC, only 12.3 and 10.0 percent of Americans are meeting recommended intake values for fruits and vegetables, respectively. As Americans continue to consume more ultra-processed foods, communicating healthy nutritional guidelines only becomes more important. While people can get nutritional advice from professionals, those services can be unaffordable and inconvenient.

## What it does
NutriSync contains two functionalities, which both aim to provide free and personalized nutritional information:

1. The **Diet Balancer** takes in a user's biometric information and food consumption and determines if that person is meeting their daily nutritional requirements in 13 different metrics. It then provides a summary of their nutritional health and generates a complementary healthy recipe to balance their diet. Lastly, it lists specific nutritional deficiencies and suggests foods rich in those nutrients.
2. The **Diet Advisor** answers questions associated with nutrition and health, keeping track of previous questions and responses to further enhance its replies. It can also provide responses in 6 differing tones.

## How we built it
We built NutriSync using the OpenAI API, Streamlit, the Requests library, the BeautifulSoup 4 library, and Python.

In Diet Balancer, a biometric profile is created and stored for later use. Up to 10 foods currently part of the user's diet are input and stored. Combining the biometric profile and diet data, a prompt is engineered, asking the large language model to determine which nutrients were sufficiently and insufficiently represented in the user's diet, which foods contribute to a good diet already, suggestions of foods to correct the user's diet, and a recipe that can use these supplemental foods as ingredients. A call to the OpenAI API is made, and a JSON object is received in response. The program parses the JSON in order to display the suggested information. The Requests library is used to find images related to listed food items by web-scraping Google Images.

As for Diet Advisor, a text field takes questions from the user, which is passed to an OpenAI API call. The program then displays the response of the API call in the user interface. Moreover, different tones of the response messages were created by altering the "content" field of the API system.

## Challenges we ran into
This is the first hackathon for most of us, so we initially had some trouble with Git and the OpenAI library. Additionally, it took us a significant amount of time to narrow down our ideas into something specific and executable in the given timeline of the hackathon.

## Accomplishments that we're proud of
Once again, this is our first hackathon, and we are proud to have used OpenAI and Streamlit to create two intuitive and useful web page in such a short period of time. Additionally, we were able to implement additional features such as web scraping to find images of recommended foods and customizing the tone of the chatbot.

## What we learned
We learned how to work with tools such the OpenAI API, Streamlit, and BeautifulSoup 4. We also learned about how we could apply AI towards the field of Health and Wellness, and had the great experience of learning what a hackathon is like.

## What's next for NutriSync
Some ideas we have for improving NutriSync include making it more accessible to more people by providing translations to different languages and incorporating disability accessibility. Other ways we are looking into improving NutriSync include adding more micronutrients, taking into consideration the quantity of each food consumed, and providing specific values for the amounts of each nutrient consumed.
