import csv
def save_results_to_csv(results, filename):
    """
    Writes out the results list of dicts to a CSV file.
    """
    if not results:
        return  # no data
    keys = results[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)