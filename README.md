## Project README — LangChain Store Finder

### Summary
A small sandbox project for me to learn how to use LangChain to build an assistant that queries a simple stores database and recommends where to buy items based on criteria such as price, time, or distance.

### Key Features
- Natural language interface for shopping queries (e.g., "cheapest place to buy apples, show me three options")
- Simple store/inventory database backend for lookups
- Scoring and ranking by user-selected metrics (price, distance, time)
- Extensible agent pipeline using LangChain primitives

### Usage Example
- Example user prompt:
  ```
  "Find the three cheapest places to buy apples within 10 miles."
  ```
- The agent parses the request, queries the store DB, ranks results, and returns a short list with prices and distances.
