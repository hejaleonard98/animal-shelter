# Páros projekt – Animal Shelter

Ebben a projektben **ketten fogtok egy közös Python alkalmazáson dolgozni**.

A cél egy egyszerű **Animal Shelter Management App**, amelyben:

- állatokat tároltok JSON fájlban;
- elérhető állatokat tudtok megjeleníteni;
- ID alapján tudtok állatot keresni;
- örökbefogadást tudtok létrehozni;
- az örökbefogadásokat JSON fájlba mentitek;
- az örökbefogadott állat státuszát módosítjátok.

A projekt során nem csak Python-kódot írtok, hanem a Git/GitHub csapatmunkát is gyakoroljátok.

A teljes folyamat:

```text
GitHub repository
        ↓
clone
        ↓
külön branchek
        ↓
külön Python modulok
        ↓
commit + push
        ↓
Pull Request
        ↓
merge
        ↓
közös integration
        ↓
működő alkalmazás
```

A projekt során gyakoroljátok:

- `uv` projekt létrehozását;
- Git és GitHub használatát;
- collaborator hozzáadását;
- repository klónozását;
- feature brancheket;
- commitot és push-t;
- Pull Requestet;
- merge-et;
- Python modulok importálását;
- paraméterezett függvényeket;
- `return` értékeket;
- JSON fájl olvasását;
- JSON fájl írását;
- több modul összekapcsolását;
- azt, amikor **egyik függvény visszatérési értékét egy másik függvény argumentumként kapja meg**.

---

# Fontos szabály

## Ne dolgozzatok közvetlenül a `main` branchen!

Új feladat előtt:

```bash
git switch main
git pull
```

Majd készítsetek saját branchet:

```bash
git switch -c feature/branch-name
```

Munka után:

```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/branch-name
```

GitHubon:

```text
Pull Request
→ review
→ merge
```

---

# 1. Projekt létrehozása

A pár egyik tagja legyen **Student A**.

Student A hozza létre a projektet:

```bash
mkdir animal-shelter
cd animal-shelter
uv init
```

Ellenőrzés:

```bash
ls -la
```

A projektben legyen legalább:

```text
README.md
pyproject.toml
main.py
.gitignore
```

A `.gitignore` például:

```text
__pycache__/
*.pyc
.venv/
.vscode/
```

---

# 2. Git repository létrehozása

Student A:

```bash
git init -b main
git add .
git commit -m "Create starter project"
```

Ezután hozzon létre GitHub repositoryt:

```bash
gh repo create animal-shelter \
  --public \
  --source=. \
  --remote=origin \
  --push
```

---

# 3. Collaborator hozzáadása

Student A GitHubon:

```text
Repository
→ Settings
→ Collaborators
→ Add people
```

Adja hozzá Student B GitHub accountját.

Student B fogadja el a meghívást.

---

# 4. Student B klónozza a projektet

Student B:

```bash
cd ~/codecool
git clone REPOSITORY_URL
cd animal-shelter
```

Ellenőrzés:

```bash
git status
git branch --show-current
```

Az aktuális branch:

```text
main
```

Mindketten futtassátok:

```bash
uv run main.py
```

---

# 5. A projekt végső struktúrája

A végére valami ilyesmi legyen:

```text
animal-shelter/
│
├── main.py
├── README.md
├── pyproject.toml
├── .gitignore
│
├── data/
│   ├── animals.json
│   └── adoptions.json
│
└── shelter/
    ├── __init__.py
    ├── animals.py
    └── adoptions.py
```

---

# 6. Student A feladata – Animals

Student A az **állatok kezeléséért** felel.

## Branch

```bash
git switch main
git pull
git switch -c feature/animals
```

## Hozd létre

```text
shelter/animals.py
data/animals.json
```

Ha szükséges:

```text
shelter/__init__.py
```

---

# 7. `animals.json`

Legyen benne legalább 5 állat.

Minden állat ilyen jellegű adatokat tartalmazzon:

```json
{
  "id": 1,
  "name": "Buddy",
  "type": "dog",
  "age": 3,
  "available": true
}
```

Az `id` minden állatnál legyen különböző.

---

# 8. Student A függvényei

Készítsd el:

```python
def load_animals(file_path):
    pass


def save_animals(file_path, animals):
    pass


def show_animals(animals):
    pass


def get_available_animals(animals):
    pass


def find_animal_by_id(animals, animal_id):
    pass


def update_animal_status(animals, adoption):
    pass
```

## `load_animals(file_path)`

Feladata:

- megnyitja a megadott JSON fájlt;
- beolvassa az állatokat;
- visszatér az állatok listájával.

## `save_animals(file_path, animals)`

Feladata:

- megkapja a fájl elérési útját;
- megkapja az állatok listáját;
- elmenti JSON fájlba.

## `show_animals(animals)`

Feladata:

- kiírja az állatok fontos adatait.

## `get_available_animals(animals)`

Feladata:

- megkapja az állatok listáját;
- csak azokat gyűjti össze, amelyeknél:

```python
available == True
```

- visszatér az elérhető állatok listájával.

## `find_animal_by_id(animals, animal_id)`

Feladata:

- megkeresi a megadott ID-jú állatot;
- ha megtalálja, visszatér az állat dictionaryvel;
- ha nem találja, térjen vissza `None` értékkel.

## `update_animal_status(animals, adoption)`

Feladata:

- megkapja az állatok listáját;
- megkap egy örökbefogadási adatot;
- megkeresi a megfelelő állatot;
- módosítja:

```python
"available": False
```

---

# 9. Student A – commit és push

```bash
git status
git add .
git commit -m "Add animal management"
git push -u origin feature/animals
```

Ezután:

```text
Pull Request
→ Student B review
→ merge
```

---

# 10. Student B feladata – Adoptions

Student B az **örökbefogadások kezeléséért** felel.

## Branch

```bash
git switch main
git pull
git switch -c feature/adoptions
```

## Hozd létre

```text
shelter/adoptions.py
data/adoptions.json
```

Az `adoptions.json` indulhat:

```json
[]
```

---

# 11. Student B függvényei

Készítsd el:

```python
def load_adoptions(file_path):
    pass


def save_adoptions(file_path, adoptions):
    pass


def create_adoption(animal, adopter_name):
    pass


def add_adoption(adoptions, adoption):
    pass


def show_adoptions(adoptions):
    pass
```

## `load_adoptions(file_path)`

Olvassa be a JSON fájlt, és térjen vissza az örökbefogadások listájával.

## `save_adoptions(file_path, adoptions)`

Mentse el a kapott listát JSON fájlba.

## `create_adoption(animal, adopter_name)`

Ez a függvény **nem keres állatot**.

Egy már megtalált:

```python
animal
```

dictionaryt kap argumentumként.

Készítsen például ilyen dictionaryt:

```json
{
  "animal_id": 1,
  "animal_name": "Buddy",
  "adopter": "Anna"
}
```

Majd térjen vissza vele.

## `add_adoption(adoptions, adoption)`

Adja hozzá az új örökbefogadást az örökbefogadások listájához.

## `show_adoptions(adoptions)`

Írja ki az eddigi örökbefogadásokat.

---

# 12. Student B – commit és push

```bash
git add .
git commit -m "Add adoption management"
git push -u origin feature/adoptions
```

Ezután:

```text
Pull Request
→ Student A review
→ merge
```

---

# 13. Közös integráció

Most mindketten:

```bash
git switch main
git pull
```

Ellenőrizzétek, hogy már minden fájl megvan:

```text
animals.py
adoptions.py
animals.json
adoptions.json
```

---

# 14. A kötelező adatfolyam

A programban történjen meg ez:

```text
find_animal_by_id()
        ↓
      animal
        ↓
create_adoption()
        ↓
     adoption
        ↓
update_animal_status()
```

Vagyis:

```python
animal = find_animal_by_id(...)
```

Student A függvényének eredménye menjen tovább:

```python
adoption = create_adoption(animal, adopter_name)
```

Student B függvényének eredménye pedig:

```python
update_animal_status(animals, adoption)
```

függvény argumentuma legyen.

Ez kötelező része a feladatnak.

---

# 15. Közös integration branch

Student A:

```bash
git switch main
git pull
git switch -c feature/integration
```

Készítse el az integráció első részét.

Például:

- importok;
- JSON adatok betöltése;
- menü alapja.

Majd:

```bash
git add .
git commit -m "Start application integration"
git push -u origin feature/integration
```

---

# 16. Student B csatlakozik az integration branchhez

Student B:

```bash
git fetch origin
git switch --track origin/feature/integration
```

Ha a branch már létezik lokálisan:

```bash
git switch feature/integration
```

Student B folytassa:

- input kezelés;
- keresés;
- örökbefogadás létrehozása;
- státusz módosítása;
- mentés;
- eredmény kiírása.

Majd:

```bash
git add .
git commit -m "Complete application integration"
git push
```

---

# 17. A `main.py` feladata

A végső program legalább ezt tudja:

```text
1. Show available animals
2. Adopt animal
3. Show adoptions
4. Exit
```

A `main.py`-ban importáljátok a szükséges függvényeket.

Például:

```python
from shelter.animals import ...
from shelter.adoptions import ...
```

A `...` helyére nektek kell kiválasztani a szükséges függvényeket.

---

# 18. JSON mentés

Ha egy állatot örökbe fogadtak, akkor mindkét adatot frissíteni kell:

```text
animals.json
+
adoptions.json
```

Ha bezárjátok és újra elindítjátok a programot, az előző örökbefogadás maradjon meg.

---

# 19. Code Review

Minden Pull Requestet a másik csapattag nézzen át.

Ellenőrizzétek:

- megfelelő branchet merge-eltek-e;
- csak a szükséges fájlok módosultak-e;
- érthetőek-e a function nevek;
- paramétereket használnak-e;
- van-e megfelelő `return`;
- működik-e a JSON olvasás;
- működik-e a JSON írás;
- nincs-e duplikált logika;
- fut-e a program.

---

# 20. Végső Pull Request

Ha elkészült az integration branch:

```bash
git status
git push
```

GitHubon:

```text
feature/integration
        ↓
       main
```

Pull Request.

Mindketten nézzétek át a:

```text
Files changed
```

részt.

Ha megfelelő:

```text
Merge pull request
→ Confirm merge
```

---

# 21. Merge után

Mindketten:

```bash
git switch main
git pull
git status
```

Ideális eredmény:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

# Végső ellenőrző lista

A projekt akkor kész, ha:

- [ ] `uv` projekt létrejött;
- [ ] van Git repository;
- [ ] van GitHub repository;
- [ ] Student B collaborator;
- [ ] Student B klónozta a repositoryt;
- [ ] külön feature brancheken dolgoztatok;
- [ ] van `animals.py`;
- [ ] van `adoptions.py`;
- [ ] van `animals.json`;
- [ ] van `adoptions.json`;
- [ ] JSON fájlból olvastok;
- [ ] JSON fájlba írtok;
- [ ] paraméterezett függvényeket használtok;
- [ ] használtok `return` értékeket;
- [ ] saját modulból importáltok;
- [ ] `find_animal_by_id()` eredménye továbbmegy a `create_adoption()` függvénynek;
- [ ] `create_adoption()` eredménye továbbmegy az `update_animal_status()` függvénynek;
- [ ] mindketten készítettetek commitot;
- [ ] mindketten pusholtatok;
- [ ] készítettetek Pull Requestet;
- [ ] átnéztétek egymás kódját;
- [ ] merge-eltétek a változtatásokat;
- [ ] elkészült a közös `main.py`;
- [ ] újraindítás után is megmaradnak az adatok.

---

# Extra feladatok

## 1. Add animal

Készítsetek olyan funkciót, amellyel új állatot lehet hozzáadni.

Az új állat kerüljön bele:

```text
animals.json
```

fájlba.

## 2. Delete animal

Lehessen állatot törölni ID alapján.

## 3. Search by type

Például:

```text
dog
cat
rabbit
```

## 4. Statistics

Írjátok ki:

```text
Available animals: ...
Adopted animals: ...
```

## 5. Adoption date

Az örökbefogadás tartalmazzon dátumot is.

Például:

```json
{
  "animal_id": 1,
  "animal_name": "Buddy",
  "adopter": "Anna",
  "date": "2026-10-23"
}
```

## 6. Return animal

Extra nehézségként lehessen egy örökbefogadást visszavonni, és az állat újra:

```python
"available": True
```

állapotba kerüljön.

---

# A projekt legfontosabb része

Nem két külön programot írtok.

A cél:

```text
Student A kódja
       ↓
Student B kódja
       ↓
közös alkalmazás
```

A két modulnak adatot kell átadnia egymásnak.

A végén egyetlen közös programotok legyen, amelyhez **mindkettőtök munkájára szükség van**.
