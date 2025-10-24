In an effort to learn a little more about modern AI frameworks I am using this repo as a sort of sandbox in which I can experiment with LangChain.

I am going to try to use LangChain to interface with a VERY simple database with information about stores. The system can be used to then look up information pertaining to these stores.

The hope is to make the AI agent produce suggestion for where to purchase each item on a shopping list to maximize a given resource \(time, money, distance traveled)

So far the system is able to take a user's simple prosaic input such as "I want to find the cheapest place to buy apples, show me three options" and query the database based off of this request.

Based on the output, the agent will provide guidance.
