# Restaurant Orders 🍽️

## Project Context 💡
This project allows the fictional "Chapa Quente" restaurant to create personalized menus, considering the customers' dietary restrictions and availability of ingredients in stock.

### Acquired Knowledge :book:

In this project, I was able to:
- Practice the concept of Hashmaps through Python's Dict and Set data structures;
- Practice Pandas library with your DataFrame data structure;
- Practice knowledge of software testing;
- Practice Object-Oriented-Programming.


## Main Technologies 🧰
<table>
    <thead>
        <tr>
            <th>Python</th>
            <th>Pandas</th>
            <th>Pytest</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
               <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" 
                       alt="python" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://pandas.pydata.org/" target="_blank" rel="noneferrer">
                    <img
                        src="https://seeklogo.com/images/P/pandas-logo-776F6D45BB-seeklogo.com.png"
                        alt="pandas"
                        width="40"
                        height="40"
                    />
                </a>
            </td>
            <td align="center">
                <a href="https://docs.pytest.org/en/7.3.x/" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/200px-Pytest_logo.svg.png" 
                       alt="pytest" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
        </tr>
    </tbody>
</table>

## Running the application ⚙️

1. Clone the repository and enter it
```
git clone git@github.com:ImVictorM/Restaurant-Orders.git && cd Restaurant-Orders
```
2. Create the virtual environment
```
python3 -m venv .venv && source .venv/bin/activate
```
3. Install the dependencies
```
python3 -m pip install -r dev-requirements.txt
```
4. Run it!
```
python3 -m uvicorn app:app
```
To check the routes with Swagger: http://127.0.0.1:8000/docs

## Testing 🛠️
To run all tests:
```
python3 -m pytest
```
Running only one test file:
```
python3 -m pytest {test_file_path}.py
```
