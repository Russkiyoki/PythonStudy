# data frames
import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
		"Age" : [30,35,50]
}

#D and F capped because its a constructor
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# adding a neww column
df["Position"] = ["Cook", "N/A", "Cashier"]

#adding a new row 
# creates new df, now we need to merge
new_row = pd.DataFrame([{"Name" : "Sandy", "Age" : 28, "Job" : "Engineer"}],
					  index=["Employee 4"])
df = pd.concat([df, new_row])
print(df)
