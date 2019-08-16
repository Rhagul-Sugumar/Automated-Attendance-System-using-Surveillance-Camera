Face API key:
Login to Microsoft azure and get face api key 

Key = “YOUR API KEY”
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

Global variable.py:
Create a variable name called personGroupId and initialize a string to it. Eg: personGroupId = ‘test1’

Create person group.py:
Run the file in the command prompt as follows:
python “path of the file name”  

Add student.py:
Initially it gets input as student’s name and roll no from the user and stores it in a database. Then it captures the students face and takes 20 snaps and stores it in a folder named dataset. Each file will be saved with name as user and roll no of the student.

Create person.py:
PersonId for each student will be created and gets updated in the database.

Command: python (path of the create person file) user’s dataset file name.
Add person faces.py:
Each file in the dataset folder gets added to Microsoft api key and then it will be stored in a Microsoft cloud.

Train.py:
Each file in the dataset folder will be trained by Microsoft face API.

Demo.py:
This file contains 3 python files such as follows:

Detect.py
Spreadsheet.py
Identify.py
Detect.py -->  faces in the images present in the test image folder will be detected and the cropped faces in the image will be stored in the cropped folder. 
Spereadsheet.py -->  spreadsheet will be created and it contains names of the trained persons and date will be updated every day.
Identify.py --> cropped faces in the cropped folder will be matched with face API key and if it found attendance will be updated in the excel sheet.

View attendance:
reports.xlsx -->to view the attendance,go to this file. 


 

