import csv  
import json  

#This modules converts csv files to JSON for the data visualisation.

# Open the CSV  
f = open( 'FDA_Module/fda.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "Appl_No", "Trade_Name", "Ingredient", "Applicant", "Approval_Date", "Type", "Product_No", "Patent_No", "Patent_Use_Code", "Submission_Date", "Appl_Type", "Exclusivity_Code", "Exclusivity_Date", "URL", " Use Code","Use"))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print("JSON parsed!") 
# Save the JSON  
f = open( 'FDA_Module/parsed.json', 'w')  
f.write(out)  
print("JSON saved!")