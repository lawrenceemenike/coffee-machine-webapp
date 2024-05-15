# Coffee Machine App

This is a Python-based web application that simulates a coffee machine. Users can order different types of coffee drinks (espresso, latte, and cappuccino), insert coins, and the app will dispense the drink if there are enough resources and the payment is sufficient.

## Features

- User-friendly interface built with HTML, CSS, and JavaScript
- Interactive ordering process with coin insertion
- Real-time resource tracking (water, milk, coffee, and money)
- Error handling for insufficient resources or payment
- Flask backend to handle order processing and resource management

## Installation

1. Clone the repository:
2. Navigate to the project directory: cd coffee-machine app
3. Create and activate a virtual environment (optional but recommended): python -m venv env
source env/bin/activate  # On Windows, use env\Scripts\activate
4. 4. Install the required dependencies: pip install flask
  
## Usage

1. Start the Flask development server: python man.py
2. Open your web browser and go to `http://localhost:5000`.

3. You should see the Coffee Machine app interface.

4. Select a drink from the menu, insert coins, and click "Order".

5. The app will process your order and dispense the drink if the payment and resources are sufficient.

6. You can check the resource levels and profits in the "Report" section.

7. To turn off the Coffee Machine, enter "off" in the order prompt.

## Project Structure
- `app.py`: The main Flask application file containing the backend logic.
- `static/`: Directory for static files like CSS and JavaScript.
- `templates/`: Directory for HTML template files.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
