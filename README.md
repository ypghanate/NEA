# Sheet Music Generator (NEA Project)

An end-to-end web application that automatically transcribes audio files into piano sheet music. Powered by a Deep Learning model trained on classical performance datasets, this platform converts raw audio recordings into structured musical scores.

## Overview

Transcribing audio to sheet music manually is a complex and time-consuming process. This project automates Automatic Music Transcription (AMT) by processing input audio through a Long Short-Term Memory (LSTM) network to predict pitch and timing data, outputting formatted piano sheet music.

### Key Features
* **Audio-to-Score Transcription:** Upload audio files (e.g., `.wav`, `.mp3`) and generate downloadable piano sheet music.
* **Deep Learning Engine:** Uses an LSTM neural network trained on the MAESTRO dataset to detect complex temporal relationships between audio signals and musical notes.
* **Web Interface:** Interactive frontend built with Django Templates to upload files, view transcription progress, and inspect generated scores.
* **MIDI & Score Processing:** Integrates `pretty_midi` and `music21` to process symbolic audio data and format readable sheet music.

---

## Tech Stack

| Domain | Technologies |
| :--- | :--- |
| **Backend** | Python, Django |
| **Frontend** | Django Templates, HTML5, CSS3, JavaScript |
| **Machine Learning** | PyTorch, Jupyter Notebook, Google Colab |
| **Audio & Music Processing** | `pretty_midi`, `music21` |
| **Dataset** | MAESTRO (MIDI and Audio Edited for Synchronous Tracks and Organization) |

---

## Architecture & Workflow

```text
[ Audio File (.wav/.mp3) ]
          │
          ▼
[ Audio Preprocessing ] ──► (Feature Extraction)
          │
          ▼
[ PyTorch LSTM Model ]  ──► (Predicts Pitches & Timings)
          │
          ▼
[ MIDI & Score Engine ] ──► (pretty_midi & music21)
          │
          ▼
[ Rendered Sheet Music / Django Frontend Output ]

To run the project you should:

## Step 1: Clone the Repository

First, you need to get a copy of this code on your computer.

1. Open the **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
2. Type the following command and press Enter:

   ```
   git clone https://github.com/ypghanate/NEA.git
   ```

This downloads the NEA project folder to your computer.


## Step 2: Set Up the Python Environment

To keep things organized and avoid conflicts, it's best to create a virtual environment:

1. Change directory to the project folder:
   ```
   cd NEA/myproject
   ```

2. Create a virtual environment (a special folder for Python and its packages):

   **Windows:**
   ```
   python -m venv venv
   ```

   **Mac/Linux:**
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   **Windows:**
   ```
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```
   source venv/bin/activate
   ```

Your prompt should change to show you are inside the environment.



## Step 3: Install Project Dependencies

1. If a file named `requirements.txt` is present:
   
   ```
   pip install -r requirements.txt
   ```

2. If not, you may need to install manually (update package names as needed):

   ```
   pip install torch django
   ```
Do this same for all libraries, such as pytorch, pretty_midi, music21



## Step 4: Run the Project

1. Start the project by running:

   ```
   python manage.py runserver
   ```

2. After a short wait, you should see a message like:
   ```
   Starting development server at http://127.0.0.1:8000/
   ```
3. Open your web browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



## Step 6: Using the Project

- Use the web interface as needed. Instructions for usage should appear on the site.
- To stop the server, return to the terminal and press **Ctrl+C**.


## Step 7: Training the Model Using Training Data

If you want to train the model using your own training data or existing training data within the repo:

1. Prepare your training data in a suitable format or find existing dataset folder.
2. Look for a Jupyter notebook (e.g., `NEA.ipynb`) or a training script that handles model training, already defined within code (model.py).
3. To run the notebook:
   - Make sure you have Jupyter installed:  
     ```
     pip install notebook
     ```
   - Start Jupyter Notebook:
     ```
     jupyter notebook NEA.ipynb
     ```
   - In your browser, open the notebook and follow the instructions to execute the training cells.
  
   - You can also use google colab to train the model
   - 
4. After training, save the output model (for example, as `simplifier_model.pth`) in the `myproject/` directory to use it with the web app.



## Additional Notes

- The file `simplifier_model.pth` is a machine learning model used by this project.
- `NEA.ipynb` is a Jupyter notebook that may include full code and instructions for training and experimentation.
