# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889


# Dictionary containing authors and the year they died
authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889
}

# Loop through each author and their corresponding death year in the dictionary
for author, date in authors.items():
# Print the author's name and the year they died using formatted string
    print(f"{author} died in {date}.")
