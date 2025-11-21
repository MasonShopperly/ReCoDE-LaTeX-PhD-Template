```latex
\input{preamble.tex}

% -------------------------------
% Page style: centered page numbers at bottom
% -------------------------------
\usepackage{fancyhdr}       %Loads the fancyhdr package, which gives you full control over page headers and footers.
                            %Define rich headers/footers with text, page numbers, section/chapter titles, etc.
                            %Position content using L/C/R (Left, Center, Right) and O/E (Odd, Even) slots (e.g., LE, RO).
                            %Add or remove header/footer rules (lines) and control their thickness.
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\begin{document}

% -------------------------------
% Title page (page number should appear)
% -------------------------------
\pagenumbering{arabic}
\setcounter{page}{1}
\input{titlepage.tex}


% Dedication / Epigraph
\thispagestyle{plain}
\vspace*{5cm}
\begin{center}
    \emph{To my family,\\
    and friends.}
\end{center}
```
