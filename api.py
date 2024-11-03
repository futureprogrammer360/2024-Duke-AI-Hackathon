import openai;
from openai import OpenAI
from dotenv import load_dotenv
import os

class AI:
    load_dotenv()
    messages = []
    api_key = os.getenv("OPEN_AI_API_KEY")
    openai_client = OpenAI(api_key=api_key)  

    def setPrompt(self,style):
        if(style == "Standard"):
            self.messages.append({"role":"system","content": "You are a professional dietician who is trying their best to help people become the best versions of themselves"})   
        elif (style == "Humorous"):
            self.messages.append({"role":"system","content": "You are a professional dietician who uses humor to help people become the best versions of themselves"})   
        elif (style == "Harsh"):
            self.messages.append({"role":"system","content": "You are a professional dietician who uses harshness to help people become the best versions of themselves"})   
        elif (style == "Sympathetic"):
            self.messages.append({"role":"system","content": "You are a professional dietician who uses sympathy to help people become the best versions of themselves"})   
           


    def get_completion_openai(self,prompt, model="gpt-4o-mini"):
        self.messages.append({"role": "user", "content": prompt})
        response = self.openai_client.chat.completions.create(model=model,messages=self.messages, temperature=1) 
        # this is the degree of randomness of the model's output) 
        self.messages.append({"role":"assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content
    
    def create_prompt(self,age, gender, weight, height, activity_level,foodList):
        prompt = f"""I am {age} years old, {gender}, weigh {weight} pounds, {height} inches tall, and {activity_level} activity. 
        For a meal, I am eating {", ".join(foodList[:-1]) + ", and " + foodList[-1]+ "."} 
        Can you tell me if I am consuming enough proteins, carbohydrates, fats, calcium, iron, fiber, 
        vitamin A, vitamin K, vitamin C, vitamin B, vitamin D, potassium, magnesium, and water, 
        what nutrients I am not consuming enough of, and suggest foods I should supplement my meal with.
        Please do so in the form of JSON; do not output any other texts before or after the JSON object.
        The JSON contains a field "summary" containing a brief summary of any nutritional deficincies I may have.
        Then, the JSON has a recipe object that contains a field "name" for the dish the recipe creates,
        a field "ingredients" which is a list of ingredients in the dish, and a field "instructions" 
        which is a list of instructions needed to cook the dish. Additionally, the JSON contains one object for each nutrient.
        For every nutrient object, there is a field "sufficient" which is true if the nutrient is sufficiently represented or false if it is not,
        another field "food_contributors" containing a list of the foods that contribute to the nutrient's sufficiency (this list is empty for insufficient nutrients),
        as well one last field, "recommendations" which contains a list of additions to the meal if that nutrient is insufficient.
        """
        print(prompt)
        return prompt

    def main(self,age,gender,weight,height,activity_level,foodList):
        """
        question = input("What is your question ")
        while(question!=""):
            print(self.get_completion_openai(question))
            question = input("What is your question ")
            """
        return self.get_completion_openai(self.create_prompt(age=age,gender=gender,weight=weight,height=height,activity_level=activity_level,foodList=foodList))
   

    
# Example of running the main method
if __name__ == "__main__":
    ai_instance = AI()  # Create an instance of the AI class
    print(ai_instance.main(age=18,gender="male",weight=155,height=6,activity_level="moderate",foodList=["mac and cheese", "boiled potatoes", "kit kats", "hersheys", "pasta", "ravioli", "donuts", "kale"]))  # Call the main method
