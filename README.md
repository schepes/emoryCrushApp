CrushEmory - Where Crushes Come to Life 🌟
Table of Contents
Introduction
Technologies
Features
Getting Started
AWS Backend Architecture
Data Retention and Privacy
Analytics
Contributing
License
Introduction
CrushEmory is a unique social app that allows you to discover connections in a fun and exciting way. Not only can you make new friends, but you can also find matches by mentioning someone you like. If the feeling is mutual, a match is created!

Technologies
Frontend: Swift with AWS Amplify for iOS
Backend: AWS (Cognito, DynamoDB, Lambda, API Gateway, etc.)
Features
Friend View
News Feed View
Matches View
Contact List Access for Matchmaking
Real-Time Notifications
Getting Started
To get started with the development environment, follow these steps:

Clone the repository.

bash
Copy code
git clone https://github.com/YourUsername/CrushEmory.git
Navigate into the project directory.

bash
Copy code
cd CrushEmory
Install dependencies.

bash
Copy code
pod install
Open .xcworkspace with Xcode.

bash
Copy code
open CrushEmory.xcworkspace
AWS Backend Architecture
The backend services are entirely built on AWS technologies. For the authentication, we are using AWS Cognito. Data storage is handled by DynamoDB, and serverless functions are executed with AWS Lambda. Learn More

Data Retention and Privacy
We take data privacy seriously. Upon first use, the app will ask for permission to access the contact list to assist in the matchmaking feature. Learn More

Analytics
We utilize AWS Kinesis Streams and Amazon QuickSight to collect and visualize real-time user interactions for better insights and continuous improvement.

Contributing
Please read CONTRIBUTING.md for details on how to contribute to this project.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
