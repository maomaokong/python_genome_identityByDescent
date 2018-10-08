#! /usr/bin/python

import os
import json


def compare_chromosomes(json_data, compare1, compare2):
    chromosome1 = json_data['chromosomes'][compare1 - 1]['polymorphism']
    chromosome2 = json_data['chromosomes'][compare2 - 1]['polymorphism']

    print()
    print("Comparing first chromosome ({0}) with second chromosome ({1})"
          .format(chromosome1, chromosome2))

    no_match = 0
    matching_ind = 0
    matching_start = 0
    matching_end = 0

    # Start comparing one character by character from first position
    for x, y in zip(chromosome1, chromosome2):
        if x == y:
            no_match += 1

            if matching_start == 0:
                matching_start = matching_ind

            matching_end = matching_ind
        else:
            no_match = 0
            matching_start = 0
            matching_end = 0

        matching_ind += 1

        if no_match > 20:
            print()
            print("No of matched: {0}".format(no_match))
            print("Matching Start: {0} and End: {1}".format(matching_start + 1, matching_end + 1))


def main():
    """
    Read the configurations from setting file
    """
    setting_file = os.path.dirname(os.getcwd()) + '/setting.json'
    with open(setting_file) as sf:
        settings = json.load(sf)

        data_folder_path = settings['data_folder_path']
        data_file_name = settings['data_file_name']
        accepted_polymorphisms = settings['accepted_polymorphisms']
        first_chromosome = settings['first_chromosome']
        second_chromosome = settings['second_chromosome']

    """
    Read the sample data from data file
    """
    data_file = os.path.dirname(os.getcwd()) + data_folder_path + data_file_name
    with open(data_file) as df:
        chromosomes = json.load(df)

    compare_chromosomes(chromosomes, first_chromosome, second_chromosome)


if __name__ == '__main__':
    main()
