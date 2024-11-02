

make sure from python install 
if you have python before version 3 just use the following command
- python --version
if you have python version 3 or late, just use the following command
- python3 --version
for pytest examples and tests, just use the following commands to install
- brew install pytest >> if you have installed brew before
- pip3 install pytest >> if you're using pip to install libs

**pytest commands**

- if you need to generate the HTML report using pytest, you should install this lib >>> pip3 install pytest-html
- if you need to run test cases and generate the html report, you should use >>  python3 -m pytest --html=report.html 
- if you need to run parallel test cases using pytest you should install xdist using this command >> pip3 install pytest-xdist
- for run test cases in parallel use this command >> python3 -m pytest -n 3 >> this will run tests across 3 threads 

**API tests**
- if you need to do api test just install requests lib using this command >> pip3 install requests
- run you tests using the basic command for run python3 -m pytest your_file_path