RequirePackage can be used before documentclass but usepackage cannot. [^1]
[^1]: [refernce from stackexchange](https://tex.stackexchange.com/questions/19919/whats-the-difference-between-requirepackage-and-usepackage)

**PLEASE** use full relative path for `\input` command to let the latex-workshop *track the structure* of the document

# metadata
The description in `hyperxmp` is `pdfsubject`. 

# align text with `align` environment
Use `&&`

# tikz--drawing language
## traverse
`\foreach \s in {#1}{func(\s)}` is substituting values from `#1` to `\s` in the second curly braces that contains `\s` one by one.
## calculation of angles
Check [this](file:///Users/veritas/scholar/G11-Semester2/Mathematics/Communication/tex/core.tex) to get to know the source.


## intersections 
The command `path[name intersections={of=<shape1> and <shape2>, name=I}];` names the the intersection *set* as `I`. All intersection *points*, from left to right, are named `(I-1),(I-2),...,(I-n)`, where `n` **equals the number of intersections**.

## How to get the x&y values of a coordinate:
From GPT
```
\path (#1);
\pgfgetlastxy{\Px}{\Py}
```

The constant of *pt* to *unit length* is **1unit=28.45274pt**
`\pgfmathparse{\x{I1}/28.45274}$\pgfmathresult$`

## slope your node 
[slope your node](https://tex.stackexchange.com/questions/570397/how-to-rotate-a-node-so-itll-be-parallel-to-a-line)
```tex
node[sloped] % this could help
```

## draw curly braces
[draw curly braces](https://tex.stackexchange.com/questions/435557/tikzpicture-horizontal-curly-brace)

## get an enclosed path with functions
```
\fill[pattern=north east lines,pattern color=green, opacity=0.6] (1,1) -- (2,2) -- (4,2) --cycle;
```

## draw at the center of a triangle
[centering](https://tex.stackexchange.com/questions/593614/draw-at-the-center-of-a-triangle-tikz)

# code printing
The key is the package named `lstlistings`. You can simply use the `\input` to print the code. But before that you should firstly declare the language of the program using `\lstset{language=<desired-language>}`

# different fonts




# use of `latexml` to convert into web markup languages
```bash
latexml document.tex --includestyles --dest=latexml/document.xml
cd latexml
latexmlpost document.xml --dest=document.xhtml --splitat=chapter
cd ../
ebook-convert latexml/document.xhtml document.epub --enable-heuristics --cover=figures/cover/coverpage-USletter.png --title "北王家村村志" --authors "王淦弘,《北王家村村志》编委会"
```


# references
I had some questions on how to use tikz to draw when:
1. doing [this math homework](file:///Users/veritas/scholar/G11-Semester1/Mathematics/Integration_Areas/main.tex)
2. drawing [this econ diagram](file:///Users/veritas/scholar/Internal-Assessment/Economics/macroeconomics/Paper/figures/AD_AS.tex)
3.  

