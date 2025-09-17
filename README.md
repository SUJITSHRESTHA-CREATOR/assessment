## Full Stact Engineer Assessment

Chrome extension and a backend service that allows a user to type a natural language instructions (eg: Give me the title, rating and price from the website) and extract data from the rendered HTML of the current tab.


## How to RUN
1. create a virtual environment

2. navigate to the server folder

3. replace the origins from the allow_origins=origins part  from app.py in server i.e. the following:
        app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

4. start the backend typing: uvicorn app:app --reload

5. load 'extension' chrome and go to developer mode and load unpacked extension

6. then type instruction in popup (eg. give me the title, price) and if not seen popup select web extractor from the extension.

7. see the JSON response and save record.
