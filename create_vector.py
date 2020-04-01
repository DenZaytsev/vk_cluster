import re
import csv

def count_word_re(string, word):
    substring_re = '(?=(%s))' % re.escape(word)
    return len(re.findall(substring_re, string))


def main():
    feature = ""
    feature_list = feature.split(',')
    with open('content_without_NAN.csv', 'r') as read_file, open('lgbt.csv', 'w', newline='') as write_file:
        write_file.write(f",id,name,{feature}\n")
        write_csv = csv.writer(write_file)
        for line in read_file:
            line = line.strip().split(",")
            text = line[3]

            row = line[:3] + [count_word_re(text.lower(), word) for word in feature_list]

            write_csv.writerow(row)


if __name__ == "__main__":
    main()