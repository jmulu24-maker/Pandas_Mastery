import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned supermarket data
df = pd.read_csv("Cleaned_supermarket.csv")

# Calculate total sales per branch
branch_sales = df.groupby("Branch")["Total_Sales"].sum()

# Create the bar chart
plt.figure(figsize=(9, 5))
branch_sales.sort_values(ascending=False).plot(
    kind="bar",
    title="Total Sales by Supermarket Branch"
)

# Add labels
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig("sales_by_branch.png", dpi=300)

# Display chart
plt.show()