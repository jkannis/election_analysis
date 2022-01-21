# Election Analysis

## Overview of Election Audit
The purpose of this project is to audit the provided tabulated results for a Colorado congressional districts election to certify the results. This analysis provides statistics and details about the counties and candidates involved in the election, as well as election results.

## Election Audit Results
- There were 369,711 total votes cast in this election.
- There are three counties in this congressional district.
    - Jefferson with 10.5% of votes cast
    - Denver with 82.8% of votes cast
    - Arapahoe with 6.7% of votes cast
- Denver had the largest turnout in this election.
- Three candidates ran in this race.
    - Charles Casper Stockham had 23.0% of votes cast
    - Diana DeGette had 73.8% of votes cast
    - Raymon Anthony Doane had 3.1% of votes cast
- Diana DeGette was the winner of this election, with 73.8% of the vote and 272,892 votes.

Election results output generated from this script
![Colorado Congressional Districts Election Results](https://github.com/jkannis/election_analysis/blob/main/Resources/ElectionResults.png)

## Election Audit Summary
- While this script was written specifically to audit the Colorado congressional districts election, some minor modifications could be made to make it usable for any election.
    - Since this script reads a csv input file of election data, any data could be passed in for processing. If the data being passed in is in the same format as this file with locale in the second column and candidate in the third column, then very little script modification would be required to process and tabulate the results. ![Input file read](https://github.com/jkannis/election_analysis/blob/main/Resources/Script_reuse_1.png) ![File column read example](https://github.com/jkannis/election_analysis/blob/main/Resources/Script_reuse_3.png)
    - If this script were to be used for a district other than a county modifications to the output details would be required. For example, 'county' would need to be changed to whatever the district type is for the election being audited. ![Output details example](https://github.com/jkannis/election_analysis/blob/main/Resources/Script_reuse_2.png)

