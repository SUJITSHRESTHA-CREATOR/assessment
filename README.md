## Full Stact Engineer Assessment

Chrome extension and a backend service that allows a user to type a natural language instructions (eg: Give me the title, rating and price from the website) and extract data from the rendered HTML of the current tab.


## How to RUN
1. create a virtual environment
2. navigate to the server folder
3. start the backend typing: uvicorn app:app --reload
4. load 'extension' chrome and go to developer mode and load unpacked extension
5. then type instruction in popup (eg. give me the title, price) and if not seen popup select web extractor from the extension.
6. see the JSON response and save record.
