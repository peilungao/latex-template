RequirePackage can be used before documentclass but usepackage cannot. [^1]
[^1]: [refernce from stackexchange](https://tex.stackexchange.com/questions/19919/whats-the-difference-between-requirepackage-and-usepackage)

**PLEASE** use full relative path for `\input` command to let the latex-workshop *track the structure* of the document

# metadata
The description in `hyperxmp` is `pdfsubject`. REALLY IMPORTANT to remember.

# tikz
## traverse
`\foreach \s in {#1}{func(\s)}` is substituting values from `#1` to `\s` in the second curly braces that contains `\s` one by one.

## intersections 
The command `path[name intersections={of=shape and shape, name=I}];` names the the intersection *set* as `I`. All intersections *points*, from left to right, are named `(I-1),(I-2),...,(I-n)` where `n` **equals the number of intersections**.

## calculating the x,y coordinates of a point
The constant of *pt* to *unit length* is **1unit=28.45274pt**
`\pgfmathparse{\x{I1}/28.45274}$\pgfmathresult$` [^2]

[^2]: [reference from stackexchange](https://tex.stackexchange.com/questions/434552/tikz-display-coordinate-of-node-using-let-command)


# code printing
The key is the package named `lstlistings`. You can simply use the `\input` to print the code. But before that you should firstly declare the language of the program using `\lstset{language=<desired-language>}`
