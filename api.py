import openai;
from openai import OpenAI
from dotenv import load_dotenv
import os

class AI:
    load_dotenv()
    messages = [{"role":"system","content": "You are an AI assistant"}]
    api_key = os.getenv("OPEN_AI_API_KEY")
    openai_client = OpenAI(api_key=api_key)        


    def get_completion_openai(self,prompt, model="gpt-4o-mini"):
        self.messages.append({"role": "user", "content": prompt})
        response = self.openai_client.chat.completions.create(model=model,messages=self.messages, temperature=1) 
        # this is the degree of randomness of the model's output) 
        self.messages.append({"role":"assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content
    
    def create_prompt(self,age, gender, weight, height, activity_level):
        prompt = f"""I am {age} years old, {gender}, weigh {weight} pounds, {height} feet tall, and {activity_level}. 
        For a meal, I am eating mac and cheese, boiled potatoes, and drinking water. 
        Can you tell me if I am consuming enough proteins, carbohydrates, fats, calcium, iron, fiber, 
        vitamin A, vitamin K, vitamin C, vitamin B, vitamin D, potassium, magnesium, and water, 
        what nutrients I am not consuming enough of, and suggest foods I should supplement my meal with.
        Please do so in the form of JSON, in which there is one object for each nutrient. 
        For the nutrients that are sufficiently represented, their objects will have one field for if it is sufficient or not, 
        and another field containing a list of the foods that contribute to the nutrient's sufficiency,
         as well as any recommendations for additions to the meal if that nutrient is insufficient. 
        For the nutrients that aren't sufficiently represented, their objects will have a field telling if it is sufficient or not,
        and another field for suggestions, which gives a list of objects with two fields, the name of the food, and the nutrients that the food has.
        return prompt"""

    def main(self):
        question = input("What is your question ")
        while(question!=""):
            print(self.get_completion_openai(question))
            question = input("What is your question ")
   

    
# Example of running the main method
if __name__ == "__main__":
    ai_instance = AI()  # Create an instance of the AI class
    ai_instance.main()  # Call the main method
