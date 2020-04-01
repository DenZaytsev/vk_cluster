import re
import csv


def count_word_re(string, word):
    substring_re = '(?=(%s))' % re.escape(word)
    return len(re.findall(substring_re, string))


def main():
    feature = "труд,офис,плат,деньг,отдых,дел,професси,учеб,комп,рутин,график,отпуск,жизн,устал,карьер,будн,ваканс,раб,пот,дом,обязан,фриланс,успех,занят,служ,волк,сила,каторг,утр,лошад,энерг,обед,самореал,действ,лен,результат,завод,ответствен,начальни,стаж,резюм,дмс,оформл,лабор"
    feature_list = feature.split(',')
    with open('content_without_NAN.csv', 'r') as read_file, open('RABota.csv', 'w', newline='') as write_file:

        write_csv = csv.writer(write_file)
        write_csv.writerow(['', "id", 'name'] + feature_list)

        for line in read_file:
            line = line.strip().split(",")
            text = line[3]

            row = line[:3] + [count_word_re(text.lower(), word) for word in feature_list]

            write_csv.writerow(row)


if __name__ == "__main__":
    main()