<h1>OrderHub</h1>
<hr>
<p>Script has been designed to automate the order processing when multiple
order files are received.
<br>
Key features of the script:

1. Extraction data such as order number, part numbers, part names, quantity, and cost
from multiple tables in multiple order files and creating collection document through tablerReader module.
2. Creating checklist through checklist module to make collection easier.
3. Dividing and sorting drawings by order, and raw material type that need to be used in production
4. Creating and reading log of performed tasks
<br>

Implemented modules:
<hr>
<h2>Table reader</h2>

<hr>
<p>Script created to automate work with multiple order files.<br>
Main reason to create this script was to automate the monotonous 
work of creating the stock issue confirmation document.
<br>
Script is able to scrape information from .doc and .docx order documents
<br>
and create output .xlsx spreadsheet with data as table ready to be copied to CI document.
<br></p>
<hr>
<p>Script significantly reduced the working time with client orders.</p>
<hr>
<p>Sample output file:</p>
<img style="max-width:1000px; width:50%;" src="sample/sample.png">
