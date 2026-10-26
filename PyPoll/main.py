import os
import csv

# File path
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

total_votes = 0
vote_counts = {}

# Skip the header and read the data
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in vote_counts:
            vote_counts[candidate] = 0

        vote_counts[candidate] += 1

# Find winner
winner = max(vote_counts, key=vote_counts.get)

# Build output
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")


for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Convert list to string for printing and writing to file
output = "\n".join(results)

# Print to terminal
print(output)

# Export to text file
output_path = os.path.join("PyPoll", "analysis", "election_results.txt")

with open(output_path, "w") as txtfile:
    txtfile.write(output)

print(f"Results saved to {output_path}\n")