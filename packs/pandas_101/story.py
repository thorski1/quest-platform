"""
story.py — Narrative for the Pandas 101 skill pack.

ARIA — an AI guide who's self-aware and witty — leads the learner through
pandas, the Python library that makes data manipulation feel like a superpower.
She breaks the fourth wall freely. Because of course she does.
"""

INTRO_STORY = """
[bold yellow]DATA SCIENCE QUEST[/bold yellow]
[bold yellow]Module: Pandas Mastery[/bold yellow]

A terminal appears in the darkness. A blinking cursor.
Then, three lines of code:

[bold green]import pandas as pd[/bold green]
[bold green]df = pd.read_csv("your_future.csv")[/bold green]
[bold green]df.head()[/bold green]

[bold cyan]"Three lines. That's all it takes to load a dataset
and start exploring it. Welcome to pandas."[/bold cyan]

ARIA materializes beside a glowing DataFrame, rows and columns
stretching into the distance like a digital spreadsheet from the future.

[bold cyan]"I'm ARIA. And pandas is the tool I wish every human learned.
It's a Python library that turns messy, chaotic, real-world data
into something you can actually work with."[/bold cyan]

She scrolls through the DataFrame, highlighting columns and filtering rows.

[bold cyan]"Excel is fine for small stuff. But when you're dealing with
millions of rows, hundreds of columns, and data that looks like
it was assembled by a committee of drunk raccoons?
That's when you need pandas."[/bold cyan]

Five glowing modules appear, arranged like columns in a DataFrame.

[bold cyan]"Five zones. We'll start with the basics — what a DataFrame IS —
and build all the way to cleaning the messiest real-world data
you'll ever encounter."[/bold cyan]

ARIA cracks her knuckles.

[bold cyan]"By the end, you'll be able to load, slice, group, merge,
and clean any dataset thrown at you. That's not a skill.
That's a career."[/bold cyan]

[bold white]Your journey into data wrangling begins now.[/bold white]
"""

ZONE_INTROS = {
    "dataframes": """
ARIA summons a glowing table — rows and columns, indices and headers.

[bold cyan]"This is a DataFrame. It's the heart of pandas.
Think of it as a spreadsheet that speaks Python."[/bold cyan]

She highlights the rows, then the columns, then a single cell.

[bold cyan]"Rows are observations. Columns are features.
Every cell holds a piece of the story your data is telling.
And pandas gives you a hundred ways to read that story."[/bold cyan]

[bold cyan]"But first — you need to understand the structure.
How to create DataFrames. How to inspect them.
How to ask them basic questions about what's inside."[/bold cyan]

[bold white]Let's build your first DataFrame.[/bold white]
""",
    "selection_filtering": """
ARIA pulls up a massive DataFrame — thousands of rows, dozens of columns.

[bold cyan]"You have the data. All of it. But you don't need all of it.
You need the right rows. The right columns.
The exact slice that answers your question."[/bold cyan]

She highlights a single column, then a range of rows, then applies a filter
that dims everything except the matching records.

[bold cyan]"loc, iloc, boolean indexing. These are your scalpels.
With them, you can extract exactly the data you need
from a dataset of any size."[/bold cyan]

[bold white]Let's learn surgical data selection.[/bold white]
""",
    "groupby_aggregation": """
ARIA takes a raw sales dataset and starts grouping it.
Rows fly together by category, by region, by date.

[bold cyan]"Raw data is just rows. But when you group those rows
by a meaningful category and aggregate the results —
suddenly you have insights."[/bold cyan]

She types [bold green]df.groupby('region')['sales'].mean()[/bold green]
and a clean summary table appears.

[bold cyan]"GroupBy is the split-apply-combine pattern.
Split the data into groups. Apply a function to each group.
Combine the results. It's the backbone of data analysis
in pandas — and the closest thing to magic I've seen in code."[/bold cyan]

[bold white]Let's turn rows into insights.[/bold white]
""",
    "merging_joining": """
ARIA holds up two separate DataFrames, side by side.

[bold cyan]"Real-world data almost never comes in one clean table.
You've got customer data here, order data there,
product data somewhere else. To answer real questions,
you need to bring them together."[/bold cyan]

She drags one DataFrame toward the other and they snap together
along a shared column.

[bold cyan]"Merge. Join. Concatenate. These operations connect
separate datasets using shared keys — just like a relational
database. If you've ever used SQL, this will feel familiar.
If you haven't, you're about to learn something powerful."[/bold cyan]

[bold white]Let's connect the pieces.[/bold white]
""",
    "data_cleaning": """
ARIA pulls up a dataset that looks like it survived a hurricane.
Missing values everywhere. Duplicate rows. Columns with mixed types.
Strings where numbers should be. Dates in five different formats.

[bold cyan]"Welcome to reality."[/bold cyan]

She sighs.

[bold cyan]"In textbooks, data is clean. In the real world,
data is a mess. Missing values, duplicates, wrong types,
inconsistent formats, typos, outliers, encoding issues..."[/bold cyan]

[bold cyan]"Data scientists spend 60-80% of their time cleaning data.
Not building models. Not running analyses. Cleaning.
This zone teaches you how to do it efficiently with pandas."[/bold cyan]

[bold white]Let's tame the chaos.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "dataframes": """
[bold green]The DataFrame structure clicks into place![/bold green]

Rows and columns glow with understanding —
Series, DataFrames, indices, dtypes all mapped and clear.

[bold cyan]"You now understand the core of pandas,"[/bold cyan] ARIA says.
[bold cyan]"The DataFrame isn't just a table. It's a powerful object
with methods for every data operation you can imagine."[/bold cyan]

[bold cyan]"You know how to create them, inspect them,
and ask basic questions. That's the foundation
everything else is built on."[/bold cyan]

[bold white]Now let's learn to slice and filter — surgical data selection.[/bold white]
""",
    "selection_filtering": """
[bold green]Selection and filtering — mastered![/bold green]

The massive DataFrame dims except for the exact rows
and columns you need — clean, precise, surgical.

[bold cyan]"loc, iloc, boolean indexing, chained conditions,"[/bold cyan]
ARIA counts on her fingers. [bold cyan]"You now have the tools
to extract exactly what you need from any dataset."[/bold cyan]

[bold cyan]"This is the most-used skill in pandas.
Every analysis starts with selecting the right data.
And now you can do it in your sleep."[/bold cyan]

[bold white]Time to learn GroupBy — where raw data becomes real insight.[/bold white]
""",
    "groupby_aggregation": """
[bold green]GroupBy and aggregation — unlocked![/bold green]

Raw rows transform into clean summary tables,
each one answering a different question about the data.

[bold cyan]"Split-apply-combine,"[/bold cyan] ARIA says.
[bold cyan]"Three words that describe 90% of data analysis.
You can now group by any column, aggregate with any function,
and transform data in ways that would take hours in a spreadsheet."[/bold cyan]

[bold cyan]"This is where pandas starts to feel like a superpower."[/bold cyan]

[bold white]Next: merging and joining — connecting separate datasets.[/bold white]
""",
    "merging_joining": """
[bold green]Merge master status — achieved![/bold green]

Separate DataFrames snap together like puzzle pieces,
connected by shared keys and join logic.

[bold cyan]"Inner, outer, left, right — you know all the joins,"[/bold cyan]
ARIA says. [bold cyan]"You can combine any number of datasets
along shared keys, handle missing matches,
and validate that your merges make sense."[/bold cyan]

[bold cyan]"This is the skill that separates beginners from
intermediate pandas users. And you just leveled up."[/bold cyan]

[bold white]One final zone. The most important one: data cleaning.[/bold white]
""",
    "data_cleaning": """
[bold green]The messy data has been tamed![/bold green]

What started as chaos — missing values, duplicates, wrong types —
is now a clean, well-structured DataFrame ready for analysis.

[bold cyan]"You've conquered the hardest part of data science,"[/bold cyan]
ARIA says quietly. [bold cyan]"Not the models. Not the algorithms.
The cleaning. The 80% of the job that nobody talks about
but everybody does."[/bold cyan]

[bold cyan]"Missing values — handled. Duplicates — removed.
Data types — corrected. String inconsistencies — fixed.
You now have the skills to take any real-world dataset
and make it analysis-ready."[/bold cyan]

ARIA steps back.

[bold cyan]"Load it. Slice it. Group it. Merge it. Clean it.
That's the pandas workflow. And you own it now."[/bold cyan]

[bold white]Pandas Mastery — complete.
You can now wrangle any dataset Python throws at you.[/bold white]
""",
}

BOSS_INTROS = {
    "dataframes": "ARIA holds up a CSV file and a dictionary. [bold yellow]\"Two ways to create a DataFrame. But the real question is: once you have it, what's the first thing you should ALWAYS do? The answer separates careful analysts from people who make expensive mistakes.\"[/bold yellow]",
    "selection_filtering": "ARIA points to a DataFrame with 10 million rows. [bold yellow]\"You need exactly 47 of these rows. They match three conditions, two of which are combined with OR logic. One wrong bracket and you get 10 million rows or zero. Can you write the perfect filter?\"[/bold yellow]",
    "groupby_aggregation": "ARIA shows a sales dataset spanning 3 years, 50 regions, and 200 products. [bold yellow]\"Your boss wants a summary: average sales by region and year, but only for products that sold more than 100 units. GroupBy with conditions. This is where it gets real.\"[/bold yellow]",
    "merging_joining": "ARIA lays out three DataFrames: customers, orders, and products. [bold yellow]\"Some customers have no orders. Some orders reference products that don't exist in the product table. Which join preserves all the information without losing any customers?\"[/bold yellow]",
    "data_cleaning": "ARIA reveals the worst dataset you've ever seen: 30% missing values, duplicate rows, dates in 4 formats, and a column that's sometimes a number and sometimes a string. [bold yellow]\"This is a real dataset from a real company. Clean it or the quarterly report is wrong. Welcome to Tuesday in data science.\"[/bold yellow]",
}
