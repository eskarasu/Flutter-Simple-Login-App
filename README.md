# Flutter Simple Login App

This repository contains a minimalistic Flutter application and a Flask server that together demonstrate a user login interface with form validation, state management, and backend authentication.

## Features

- Basic Flutter app setup with login screen
- Form input validation in Flutter
- State management with `StatefulWidget`
- Flask server for backend authentication
- Simple username and password validation

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Flutter and Dart installed on your machine
- Python and Flask installed for the backend server
- An IDE (e.g., Android Studio, VSCode, etc.)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/eskarasu/Flutter-Simple-Login-App
   ```
2. Install the required packages:
 ```
  flutter pub get
```
3. Install the required packages for Flask:
```
pip install flask
```
4. Run the Flask server:
```
python server.py
```
5. Run the Flutter app:
```
flutter run
```

## Usage

Use this simple login app as a starting point for integrating a login interface with backend authentication into your Flutter applications.

## Backend Server

The Flask server provides a simple /login endpoint that performs a basic authentication check against a predefined dictionary of users.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1.  Fork the Project
2.  Create your Feature Branch (git checkout -b feature/AmazingFeature)
3.  Commit your Changes (git commit -m 'Add some AmazingFeature')
4.  Push to the Branch (git push origin feature/AmazingFeature)
5.  Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
