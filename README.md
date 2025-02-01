# Floor Plan Generator

A simple web application that allows users to create floor plans by entering room dimensions. The app takes in the dimensions of rooms and generates a floor plan in the DXF format (a file format used for CAD drawings), which can then be downloaded for use in design applications.

## Features
- Users can enter room dimensions (width and height).
- Automatically generates a floor plan based on the provided room dimensions.
- Downloads the generated floor plan as a DXF file (AutoCAD file format).
- Built with Python, Flask, and the `ezdxf` library for generating the floor plan in the DXF format.

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, JavaScript (for interaction with the bot)
- **File Format:** DXF (AutoCAD Drawing Exchange Format)
- **Libraries:**
  - `Flask` for the web framework
  - `ezdxf` for creating the DXF file
  - `requests` for handling API requests

## Requirements

Before running this project locally, you need to install the required dependencies. This project uses a `requirements.txt` file to specify the necessary Python packages.

### Dependencies
- Python 3.x
- `Flask`
- `ezdxf`
- `requests`

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/floor-plan-generator.git
   cd floor-plan-generator
2.Create a Virtual Environment It's recommended to use a virtual environment for managing dependencies.

python3 -m venv venv

source venv/bin/activate
# On Windows: venv\Scripts\activate

3.Install Dependencies

pip install -r requirements.txt

4.Run the Application Locally

python app.py
