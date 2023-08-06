# VAI toolkit

## Quickstart

1. To add data to our platform use this package like below

`pip install vai-toolkit`

2. then add import statement like this

`from vai_toolkit import vai`

here is the code to use the plugin

Data has to be in a dictionary. With time stamps in the indicated 'dd-mm-yr'

    data = { "id": [11111, 1], "Capital Gain": [10000, 15000] }   # Columns data
    dates = ["12-15-2021", "12-16-2021"]  # Dates
    times = ["11:08:50", "11:09:50" ]  # Times

We have implemented a series of security measurements including pipeline id and security secrets which can be accessed using the following.

    pipeline = os.getenv("PIPELINE") # Pipeline
    user_secret = os.getenv("USER_SECRET") # UserSecret

Then finally, upload the data.

    res = vai.upload_data(data, dates, times, pipeline, user_secret, allow_new_columns=True, allow_duplicate=True, allow_new_category=True)

Note:

Last 3 fields are optionals (allow_new_columns, allow_duplicate, allow_new_category)