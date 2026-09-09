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
```

---

## To Run the Project

### Step 1: Clone the Repository

First, you need to get a copy of this code on your computer.

1. Open the **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
2. Type the following command and press Enter:

```bash
git clone [https://github.com/ypghanate/NEA.git](https://github.com/ypghanate/NEA.git)
```

This downloads the NEA project folder to your computer.

---

### Step 2: Set Up the Python Environment

To keep things organized and avoid conflicts, it's best to create a virtual environment:

1. Change directory to the project folder:
```bash
cd NEA/myproject
```

2. Create a virtual environment:

**Windows:**
```cmd
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

3. Activate the virtual environment:

**Windows:**
```cmd
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### Step 3: Install Project Dependencies

1. If a file named `requirements.txt` is present:
```bash
pip install -r requirements.txt
```

2. If not, install the libraries manually:
```bash
pip install torch django pretty_midi music21 notebook
```

---

### Step 4: Run the Project

1. Start the project server:
```bash
python manage.py runserver
```

2. Open your web browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### Step 5: Using the Application

* Use the web interface to upload audio files and view generated sheet music.
* To stop the server, return to the terminal and press **Ctrl+C**.

---

## Model Training & Custom Datasets

If you want to train the model using your own training data or existing dataset files:

1. Prepare your dataset in a suitable format or navigate to the project dataset folder.
2. Open the training notebook (`NEA.ipynb`) locally or in **Google Colab**:
```bash
pip install notebook
jupyter notebook NEA.ipynb
```
3. Follow the instructions within the notebook to execute the training cells.
4. After training, export the saved model weights (`simplifier_model.pth`) into the `myproject/` directory for the Django application to load.
