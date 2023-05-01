# WriteRx - Medical Note-Taking App

WriteRx is an intelligent web application designed to simplify medical documentation using OpenAI's GPT-4 language model. 
It offers an intuitive interface, smart data-entry features, customizable templates, and automated billing codes. 
WriteRx generates well-structured medical notes in the SOAP format, making it an essential tool for busy medical 
practices seeking efficient patient care.

Endpoint: [WriteRx App](https://your-app-url.com)

## Getting Started

To begin using the WriteRx application, follow the steps outlined below:

1. Clone the repository to your local machine.
2. Install [Poetry](https://python-poetry.org/docs/#installation) on your local machine if not already present.
3. Navigate to the root directory of the project and execute `poetry install` to install the required dependencies.
4. Set your OpenAI API key as a streamlit secret with the name `OPENAI_API_KEY`.
5. Run `poetry run streamlit run ./app/main.py` to initiate the application.
6. Access the application by opening the URL displayed in the console.

## Usage

WriteRx features an intuitive user interface for the seamless generation of medical notes in the SOAP format. 
Follow these steps to utilize the application:

1. Input the patient's Chief Complaint (mandatory field).
2. (Optional) Click on the "OLDCART" expander and fill in any relevant information.
3. Click the "Generate Medical Note" button to create a well-structured medical note in the SOAP format.
4. The generated note will appear below the button.

## Dependencies

WriteRx employs [Poetry](https://python-poetry.org/) for dependency management. The following packages are necessary to run the application:

- python = "3.9.16"
- streamlit = "^1.22.0"
- openai = "^0.27.5"

Access to OpenAI's language model requires an API key.

## Credits and Licensing

Developed by Shashank Kapadia, WriteRx is released under the [MIT License](https://opensource.org/licenses/MIT). 
The application utilizes OpenAI's language model, subject to OpenAI's terms of service.

## Code Attribution

If you plan to use any portion of the WriteRx source code in your own projects, please provide proper attribution by 
including the following in your documentation or source code:

```json
{
  "Project": "WriteRx - Medical Note-Taking App",
  "Developer": "Shashank Kapadia",
  "Source": "https://github.com/kapadias/write-rx",
  "License": "MIT License"
}
