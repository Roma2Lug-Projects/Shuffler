
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

import random

class QuestionAnswer(object):

    LatexTemplate = """
\\noindent
{qid}) {question}
\\begin{{enumerate}}[a.] \setlength{{\itemsep}}{{0pt}}
{items}
\end{{enumerate}}
"""

    def __init__(self, question, answer_set):

        self.question = question
        self.answer_set = answer_set
        self.answer_index = -1

        random.shuffle(self.answer_set)

        for i, answer in enumerate(self.answer_set):
            if answer.startswith('*'):
                self.answer_index = i
                self.answer_set[i] = answer.lstrip('*')
                break


        if self.answer_index == -1:
            raise Exception('Answer set doesn\'t specify the right answer!')


    def __str__(self):

        answers = ""

        for index, answer in enumerate(self.answer_set):
            answers += "{0}. {1}\n".format(index+1, answer)


        return "{0}\n{1}\n".format(self.question, answers)


    def to_latex(self, question_id = 1):

        params = dict()
        
        params['qid'] = question_id
        params['question'] = self.question
        params['items'] = ""

        for answer in self.answer_set:
            params['items'] += "\item {0}\n".format(answer)

        return QuestionAnswer.LatexTemplate.format(**params)

    def get_answer_index(self):
        return chr(97 + self.answer_index)


