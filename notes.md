`\RequirePackage` can be used before `\documentclass` but `\usepackage` cannot. [^1]
[^1]: [reference from stackexchange](https://tex.stackexchange.com/questions/19919/whats-the-difference-between-requirepackage-and-usepackage)

**PLEASE** use full relative path for `\input` command to let the latex-workshop *track the structure* of the document

# Metadata

The description in `hyperxmp` is `pdfsubject`.

# Align text with `align` environment

Use `&&`

# Tikz--drawing language

## traverse

`\foreach \s in {#1}{func(\s)}` is substituting values from `#1` to `\s` in the second curly braces that contains `\s` one by one.

Example:

```tex
\foreach \s in {1,2,3}{
  \draw (0,0) circle (\s);
}
```

## Calculation of angles

Check [this](file:///Users/veritas/scholar/G11-Semester2/Mathematics/Communication/tex/core.tex) to get to know the source.

## Intersections

### Name a path

`\draw[name path=<name>]`

### Use path names to get intersection

The command `path[name intersections={of=<shape1> and <shape2>, by=I}];` names the the intersection *set* as `I`. All intersection *points*, from left to right, are named `(I-1),(I-2),...,(I-n)`, where `n` **equals the number of intersections**.

## How to get the x&y values of a coordinate

From GPT

```tex
\path (<coordinate 1>);
\pgfgetlastxy{\Px}{\Py}
```

The constant of *pt* to *unit length* is **1unit=28.45274pt**
`\pgfmathparse{\x{I1}/28.45274}$\pgfmathresult$`

## Slope your node

[slope your node](https://tex.stackexchange.com/questions/570397/how-to-rotate-a-node-so-itll-be-parallel-to-a-line)

```tex
node[sloped] % this could help
```

## Draw curly braces

[draw curly braces](https://tex.stackexchange.com/questions/435557/tikzpicture-horizontal-curly-brace)

## Get an enclosed path with functions

```tex
\fill[pattern=north east lines,pattern color=green, opacity=0.6] (1,1) -- (2,2) -- (4,2) --cycle;
```

## Draw at the center of a shape

[centering](https://tex.stackexchange.com/questions/593614/draw-at-the-center-of-a-triangle-tikz)

```tex
\node at (barycentric cs:A=1,B=1,C=1) {D};
```

D is at the center of A, B, and C.

## 3D drawing

### Rotate the graph

Rotation used in

```tex
\begin{tikzpicture}[rotate around <axis name> = <numerical value in degrees>]
\end{tikzpicture}
```

is just **keep the *chosen axis* fix**, and **rotate *all other* elements in the graph** with that certain angle.

The order in which the axis rotation commands are place also plays a role in it.
For example,

```tex
rotate around x=-90, 
rotate around z=-90,
rotate around y=90, 
```

Is not the same as

```tex
rotate around y=90, 
rotate around x=-90, 
rotate around z=-90,
```

### Shading an arbitrary 3D object

Use the expression along one axis to draw the shape in many many slice planes perpendicular to this axis.

Example:

```tex
% Render the body of the tube
\foreach\c in {0.01,0.02,...,\ldecreA}{
  \begin{scope}[canvas is xz plane at y=\c]
    \def\majorAxis{(\d*\l+(\r-\d)*\c)/\l}
    \def\minorAxis{(\c*\r)/\l}
    \draw[thick,color=\bodyColor,opacity=0.015] (0,0) ellipse [x radius=\majorAxis, y radius=\minorAxis];
  \end{scope}
}
```

### Put text on the plane

The use of `transform shape` for node argument.

```tex
\begin{scope}[canvas is yz plane at x=0]
    \node at (1.5,0.7) [red,transform shape,scale=0.2] {$p_Y(y)$};
\end{scope}
\begin{scope}[canvas is xz plane at y=3]
    \node at (2,0.7) [blue,transform shape,scale=0.2] {$p_X(x)$};
\end{scope}
```

[reference](https://tex.stackexchange.com/questions/544417/text-along-the-planes-in-3d)

## Tikz externalizing

Externalizing tikz figures to save the time for compiling unchanged tikz graphs.

[reference](https://tex.stackexchange.com/questions/45/how-to-speed-up-latex-compilation-with-several-tikz-pictures)

> Read section 52, "Externalizing Graphics", of the PGF manual v3.1.9a.

Usage:

```tex
\usetikzlibrary{external}
\tikzexternalize
```

To refer to external standalone files, use

```tex
\begin{figure}
  \input{path/to/tikz/source/tex}
\end{figure}
```
  
# Code printing

The key is the package named `lstlistings`. You can simply use the `\input` to print the code. But before that you should firstly declare the language of the program using `\lstset{language=<desired-language>}`

# Different fonts

# Use of `latexml` to convert into web markup languages

```bash
latexml document.tex --includestyles --dest=latexml/document.xml
cd latexml
latexmlpost document.xml --dest=document.xhtml --splitat=chapter
cd ../
ebook-convert latexml/document.xhtml document.epub --enable-heuristics --cover=figures/cover/coverpage-USletter.png --title "北王家村村志" --authors "王淦弘,《北王家村村志》编委会"
```

# References

I had some questions on how to use tikz to draw when:

1. doing [this math homework](file:///Users/veritas/scholar/G11-Semester1/Mathematics/Integration_Areas/main.tex)
2. drawing [this econ diagram](file:///Users/veritas/scholar/Internal-Assessment/Economics/macroeconomics/Paper/figures/AD_AS.tex)
3.  
