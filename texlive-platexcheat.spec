%global tl_name platexcheat
%global tl_revision 49557

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	A LaTeX cheat sheet, in Japanese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcheat/platexcheat
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/platexcheat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/platexcheat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation to Japanese of Winston Chang's LaTeX cheat sheet
(a reference sheet for writing scientific papers). It has been adapted
to Japanese standards using pLaTeX, and also attached additional
information of "standard LaTeX" (especially about math-mode).

