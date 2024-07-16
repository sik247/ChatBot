# Harry's AI Q&A Demo

Welcome to Harry's AI Q&A Demo! This project is an interactive web application that allows users to ask questions and get responses from an AI model powered by OpenAI's GPT-3.5-turbo.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Harry's AI Q&A Demo is a simple and interactive web application built using Streamlit. It leverages OpenAI's GPT-3.5-turbo model to provide intelligent responses to user queries. This project demonstrates how to integrate OpenAI's language model with a web interface for real-time Q&A interactions.

## Features

- Interactive web interface for asking questions.
- Real-time responses from OpenAI's GPT-3.5-turbo model.
- Easy to set up and use.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/harrys-ai-qa-demo.git
    cd harrys-ai-qa-demo
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key to the `.env` file:
      ```env
      OPENAI_API_KEY=your_openai_api_key_here
      ```

## Usage

To start the application, run the following command:

```bash
streamlit run app.py