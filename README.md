# Sudoku (Generation/Solving/Graph representation) 🔢
Sudoku (Generation/Solving/Graph representation) provides the functionalities of generating a solved Sudoku board and representing that solved Sudoku board in the form of a matrix or in a form of a graph.

## 📕 Description
🇬🇧 ENG:
Sudoku (Generation/Solving/Graph representation) firstly generates an unsolved 9x9 Sudoku board which is then solved using one of the chosen algorithms - currently those algorithms are the Backtracking algorithm and the DSatur algorithm. Solved Sudoku board is then visually represented to the user in a form of a matrix and a graph via the Graphical User Interface made with Tkinter and the embedded Matplotlib figures.

🇭🇷 CRO:
Sudoku (Generiranje/Rješavanje/Grafovska vizualizacija) prvotno generira neriješenu 9x9 Sudoku ploču koja potom biva riješena odabranim algoritmom - trenutno implementirani algoritmi su Backtracking algoritam te DSatur algoritam. Riješena Sudoku ploča zatim se vizualno reprezentira u obliku matrice ili grafa koristeći grafičko korisničko sučelje koje je razvijeno pomoću Tkinter paketa te ugrađenih Matplotlib figura.


## How to run this? 🏁
### Dependencies
Install all the dependencies with pipenv. A list of dependencies can be found inside the _Pipfile_.
```
pipenv install
pipenv shell
```
### Run
Position yourself to the root directory (the one containing this file, Pipfile, etc.) and run the following command:
```
python -m sudoku
```

## How to use this? 😕
1. Pick a solving algorithm
2. **Tick the 9x9 radio button**. More Sudoku board sizes will be added in the future.
3. Click "Generate a solved board" button.
4. Observe the generated board as matrix or a graph.

## Screenshots 📸

