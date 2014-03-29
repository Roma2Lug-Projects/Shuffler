
"""
Shuffler v1.0, a simple question answer shuffler.

Copyright (C) 2014 Giulio Picierro for Roma2LUG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import sys
import random
import qa
from latexdoc import *


def check_arguments(argc, args):

    if argc < 3:
        print "Syntax: {0} <input file> <output file>".format(args[0])
        quit()
    else:

        return (args[1], args[2])


def parse_input_file(filename):

    qa_set = []

    f = open(filename)

    current_question = None
    answer_set = None

    for row in f:        

        if row[:2] == "Q:":

            if answer_set:
                q = qa.QuestionAnswer(current_question, answer_set)
                qa_set.append(q)

            current_question = row[3:].strip("\n")
            answer_set = []

        elif len(row) > 1:
            answer_set.append( row.strip("\n") )

    if answer_set:
        q = qa.QuestionAnswer(current_question, answer_set)
        qa_set.append(q)

    f.close()

    return qa_set


def write_output_file(filename, document):

    f = open(filename, 'w')

    f.write(document.finalize())

    f.close()


def main(argc, args):

    in_filename, out_filename = check_arguments(argc, args)

    qa_set = parse_input_file(in_filename)

    solutions = open('solutions.txt', 'w')

    sample_len = min(10, len(qa_set))

    document = LatexQuestionDocument()

    for index, student in enumerate(open('students.txt')):
        page = LatexQuestionPage("2 Aprile 2014", student.strip('\n'), index+1)

        qa_sel = random.sample(qa_set, sample_len)

        solutions.write('Questionario {0}: '.format(index+1))

        for i, qa in enumerate(qa_sel):
            solutions.write( '<{0}, {1}> '.format(i+1, qa.get_answer_index()) )

        solutions.write('\n')

        page.add_questions(qa_sel)

        document.add_page(page)

    solutions.close()

    write_output_file(out_filename, document)



if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
