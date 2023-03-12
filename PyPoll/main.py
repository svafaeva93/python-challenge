import pandas as pd 

filepath= "./PyPoll/Resources/election_data.csv"
df = pd.read_csv(filepath,sep = ",")

total_votes = df['Ballot ID'].count()
candidates = df['Candidate'].unique()

number_of_votes_per_candidate=df.groupby('Candidate').agg({'Ballot ID' : 'count'})
percentage_per_candidate = (number_of_votes_per_candidate['Ballot ID'] / total_votes) * 100
percentage_per_candidate = percentage_per_candidate.sort_values(ascending=False)
winner = percentage_per_candidate.index[0]


# Create a new DataFrame with the results
results_df = pd.DataFrame({
    'Candidate': percentage_per_candidate.index,
    'Percentage of Votes': percentage_per_candidate.values,
    'Total Votes': number_of_votes_per_candidate['Ballot ID'].values
})

# Sort the results by percentage of votes in descending order
results_df = results_df.sort_values('Candidate', ascending=True)

# Add a column with the formatted percentage of votes
results_df['Percentage of Votes'] = results_df['Percentage of Votes'].map('{:.3f}%'.format)

# Add a header with the total number of votes
header = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
'''

# Add a footer with the winner
footer = f'''
-------------------------
Winner: {winner}
-------------------------
'''

# Write the results to a CSV file
with open('./PyPoll/analysis/election_results.csv', 'w') as f:
    f.write(header)
    results_df.to_csv(f, index=False)
    f.write(footer)