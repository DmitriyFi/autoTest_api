# Basic api autotests on the "ipwhois" service.
The project consists of two folders: 
1. 'src' with subfolders:
  - 'baseclasses' : contains class Response, which by itself has some validation methods, such as:
    - validation by class Atributes_Ip inherited pydantic schema;
    - validation by api status code;
    - validation by number of api objects.
  - 'enums' : contains global and local enums for the project:
    - global enums has class GlobalErrorMessages inherited class Enum to designate some global errors which we can face during testing;  
    - local enums (ipwhois_enums) has couple of classes which we created to fix the structure of objects that the api provides us, and it's errors as well.
  - 'shcemas' : contains basic validation schema class, inherited pydantic BaseModel, which checks for matching data types of the api response generally, and validation of every single api object (I have: ip validator by version type, ContinentsAndCodes validator by existing) in particular. 
2. 'tests' with main testing script folder(I have: ipwhois): 
  - api_response.json is a copy of api's response provides we make for a good mesure;
  - conftest.py consists all fixtures we needed(I have function of getting api's response, returning response);
  -  ipwhois_test.py directly executable test script.

Also we have configuration.py with service url and requirements.txt with all packages and dependencies used during this.