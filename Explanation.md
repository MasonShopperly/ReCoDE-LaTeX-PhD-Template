### 🏛️ Title Page — Compliance with Imperial College Thesis Submission Checklist (§ 4.5)

According to the *Imperial College London Thesis Submission Checklist* (section 4.5),  
the title page **must bear the following information**:

> - The approved title of the thesis (as confirmed at the point of examination entry)  
> - The candidate’s full name, as registered at the College  
> - *Imperial College London* and the name of the Department  
> - The degree for which the thesis is submitted (e.g. PhD)

This template fully satisfies those requirements with the following LaTeX structure:

```latex
\begin{titlepage}                  % Creates a standalone title page environment.
  \centering                       % Centers all content horizontally on the page.

  \vspace*{3cm}                    % Adds 3 cm of vertical space at the top for visual balance.

  {\Huge\bfseries Title of the Thesis\par}    % Prints the thesis title in very large, bold font.
                                              % Fulfills: “Approved title of the thesis.”

  \vspace{1.5cm}                   % Adds spacing between the title and author’s name for readability.

  {\Large Your Name\par}           % Displays the candidate’s full name, as registered at Imperial College.
                                   % Fulfills: “Candidate’s full name.”

  \vfill                           % Pushes the following lines toward the bottom of the page,
                                   % ensuring balanced white space between top and bottom content.

  A thesis submitted for the degree of\\
  Doctor of Philosophy\\           % Clearly states the qualification sought.
                                   % Fulfills: “Degree for which the thesis is submitted.”

  Department / School Name\\       % Lists the candidate’s department or research group.
                                   % Fulfills: “Imperial College London and the name of the Department.”

  Imperial College London\\        % Specifies the awarding institution exactly as required.

  \vspace{1cm}                     % Adds a final vertical gap before the submission date.

  \today                           % Automatically inserts the current date of compilation
                                   % (can be replaced with the official submission date if desired).
\end{titlepage}                    % Ends the title page environment.
```




### 📄 Abstract Section — Compliance with Imperial College Thesis Submission Checklist (§ 7.1)

According to the *Imperial College London Thesis Submission Checklist* (section 7.1):

> “The title page should be followed by an abstract consisting of no more than 300 words.”

This template fully complies with that requirement.

The **Abstract** is defined in the file as:

```latex
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}
% Write your abstract here (maximum 300 words)


