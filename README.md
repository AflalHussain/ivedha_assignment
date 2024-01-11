### TEST 1
a) 
 - monitor.py file has the script to create the json files.
 - the files are saved inside the status_files directory

b)
Run the flask app
 -  ```pip install -r requiremnets.txt```
 -  ```python app.py```

### TEST 2

- ```ansible-playbook -i inventory.ini monitoring_playbook.yml```

### TEST 3
 - Install pandas ```pip install pandas```
 - remove 'props_less_than_average_price.csv'
    ```rm props_less_than_average_price.csv```
 - Run ```python find_props_priced_below_avg.py```