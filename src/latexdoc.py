
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

class LatexQuestionPage(object):

    LatexHeaderTemplate = """
\\begin{{center}}\\footnotesize{{Seminario {date} - Roma2LUG - Universita' di Roma Tor Vergata}}\\normalsize

\\bigskip\\textbf{{Questionario numero {qnumber} }} \hfill \\textbf{{ {stud_name} }}\\\\\\bigskip\end{{center}}"""


    def __init__(self, _date, _stud = "", _qnumber = 1):
        self.text = "\pagebreak \\newpage\n"

        self.text += LatexQuestionPage.LatexHeaderTemplate.format(date = _date, qnumber = _qnumber, stud_name = _stud)

    def add_questions(self, qa_set):

        self.text += "\\begin{minipage}[t]{0.45\\textwidth}\n"

        for index, qa in enumerate(qa_set):

            if index > 0 and index % 5 == 0:
                self.text += "\end{minipage}\n"
                self.text += "\\begin{minipage}[t]{0.05\\textwidth}\hfill\n"
                self.text += "\end{minipage}\n"
                self.text += "\\begin{minipage}[t]{0.45\\textwidth}\n"
            self.text += qa.to_latex(index+1)

        self.text += "\end{minipage}\n"

    def __str__(self):
        return self.text


class LatexQuestionDocument(object):

    def __init__(self): 

        self.text = """
\documentclass[10pt]{article}
\usepackage[margin=0.5in]{geometry}
\usepackage[italian]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage[T1]{fontenc}
\usepackage{ucs}
\usepackage[utf8x]{inputenc}
\usepackage{enumerate}

\\begin{document}\pagestyle{empty}
"""

    def add_page(self, page):
        self.text += str(page)


    def finalize(self):
        return self.text + "\end{document}"
