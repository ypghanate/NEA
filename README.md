This project explores generating sheet music that changes based on the player’s skill level. 
Most automatic music-generation tools create pieces that do not get easier or harder depending on who will play them. 
A beginner might receive sheet music with wide jumps or dense chords, while an advanced player might get something too basic.

To address this, the project trains a model on examples where difficulty is built into the data. 
Easier pieces contain fewer notes, a smaller pitch range, and simpler rhythms. 
Harder pieces use more notes, wider intervals, and more complex rhythmic patterns. 
By learning from these differences, the model can produce new music that follows similar difficulty patterns.

The system takes a selected difficulty level as input and generates a corresponding piano-roll sequence, which is then converted into MIDI and sheet music. 
The repository includes tools for generating training data, training the model, producing new pieces, and visualising piano-roll outputs to check whether difficulty is being reflected in the generated music.

The project is hosted on Django for the frontend, and uses pytorch for backend.
