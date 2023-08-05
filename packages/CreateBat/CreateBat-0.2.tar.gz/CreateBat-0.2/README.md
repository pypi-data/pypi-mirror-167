A little function to create a batch file on your desktop to run your script. 

```python
from CreateBat import create_batch_file_on_desktop
create_batch_file_on_desktop()
#After calling the function, filedialog.askopenfilename will ask for the .py file

output:


Do you want to add parameters? (e.g: --path=C:\Users )>? --check
If you want to keep the console open after executing the script, press: "y" ?>? y

Batchfile written to:
C:\Users\Gamer\Desktop\_bs4dfscraping.bat
_____________________
    @echo off
    C:
    cd "C:\Users\Gamer\anaconda3\envs\dfdir"
    echo Activating dfdir
    CALL activate dfdir
    echo Starting Python C:\Users\Gamer\anaconda3\envs\dfdir\bs4dfscraping.py
    CALL "C:\Users\Gamer\anaconda3\envs\dfdir\python.exe" -i "C:\Users\Gamer\anaconda3\envs\dfdir\bs4dfscraping.py" --check
    
Out[3]: 'C:\\Users\\Gamer\\Desktop\\_bs4dfscraping.bat'


```
