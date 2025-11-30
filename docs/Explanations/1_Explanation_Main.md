## 🎓 Introduction

The *Imperial College London Thesis Submission Checklist* outlines the essential requirements for PhD thesis formatting and structure, but it does **not provide strict or exhaustive layout specifications**.  
This leaves flexibility for candidates to decide how to design and typeset their thesis, as long as the document contains all required elements in the correct order. 

This document serves four main purposes:

1. **Explain** the official requirements defined in the Thesis Submission Checklist and related Imperial College regulations.  
2. **Demonstrate** how each requirement has been implemented in this LaTeX template — linking each rule to the corresponding code snippet or environment.  
3. **Recommend best practices** in academic typesetting, presentation, and structure to help produce a professional-quality thesis.  
4. **Empower users** to understand the reasoning behind each implementation so they can confidently make their own adjustments while remaining compliant with Imperial College’s regulations.

By combining regulatory guidance with technical explanations, this document helps PhD students not only use the provided template effectively but also **customize it responsibly**, ensuring their thesis remains compliant, well-formatted, and professionally presented.

## ⚙️ Document Settings

Every LaTeX document begins by declaring its **class**; this determines the overall structure, formatting, and layout rules used by the compiler.  
For this thesis template, the following declaration is used:

<!-- SNIPPET: documentclass -->

### 🏛️ Preamble and Title Page

Because of their length and complexity, the preamble and title page have been given dedicated pages for detailed explanation. The code snippet below loads the preamble, configures headers/footers and page numbering, and inserts the title page:

<!-- SNIPPET: preamble_title -->

### 📄 Dedication

The *Imperial College London Thesis Submission Checklist* does **not require** a Dedication page. Including one is **entirely optional**. By convention, Dedications usually appear near the beginning of a thesis, but their exact placement is flexible.

Below is the LaTeX structure used for the dedication page in this template:

<!-- SNIPPET: dedication -->

### 📜 Declaration of Originality

Imperial requires a **Statement of Originality** near the beginning of the thesis. The following snippet implements this requirement and includes a copyright statement:

<!-- SNIPPET: Declaration of Originality -->

### 📑 Abstract — Compliance with §7.1

According to the checklist, the **title page must be followed by an abstract of no more than 300 words**. The template defines the abstract section as follows:

<!-- SNIPPET: Abstract -->

### 🙏 Acknowledgements

Acknowledgements are **optional** but common. They allow you to thank supervisors, collaborators, family, friends, and funders. Imperial does not mandate their exact location.

The LaTeX structure used in this template is:

<!-- SNIPPET: Acknowledgements -->

### 📣 Dissemination

This optional section lists publications, posters and other research outputs related to the thesis:

<!-- SNIPPET: Dissemination -->

### 📚 Nomenclature & Acronyms

This template provides optional sections for **nomenclature** and **acronyms**:

<!-- SNIPPET: Nomenclature_Acronyms -->

### 📋 Contents and Lists

Imperial requires a **table of contents** and lists of figures/tables after the abstract and front matter. This template uses:

<!-- SNIPPET: Contents, List of Figures/Tables -->

### 📘 Main Chapters

The main body of the thesis is organised into numbered chapters:

<!-- SNIPPET: CHAPTERS -->

### 📎 Appendices

Appendices follow the bibliography and may include additional material and permissions:

<!-- SNIPPET: APPENDIX -->

### 📖 Bibliography

The bibliography is generated automatically from your `.bib` file:

<!-- SNIPPET: Bibliography -->


