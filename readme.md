#### Operacje do otestowania to: <br>
 <li>CRUD</li>
 <li>listowanie </li>
 <li>filtrowanie</li>


<br>
api url: <br>

```
https://jsonplaceholder.typicode.com/
```

#### Wymagania:
<li>python 3.7 or newer</li>
<li><b>python packages: </b></li>
<ul>pytest (ver. 5.3.5)</ul>
<ul>allure-pytest (ver. 2.8.10)</ul>
<li><a href="https://docs.qameta.io/allure/">allure </a></li>

<br>

##### Jak uruchomic testy:

```
<path_to_py.test> --alluredir <path_to_allure_directory> <path_to_directory_with_tests>
eg.
C:\Users\kkkuc>C:\Users\kkkuc\vodeno\Scripts\py.test.exe --alluredir "C:\Users\kkkuc\Downloads\allure" C:\Users\kkkuc\IdeaProjects\vodeno
```

##### Jak wygenerowac raport z testow:

```
allure serve <path_to_allure_reports>
eg.
allure serve "C:\Users\kkkuc\Downloads\allure"
```

W pliku api_testing_pytest+allure.swf jest filmik z wykonania testow <br>